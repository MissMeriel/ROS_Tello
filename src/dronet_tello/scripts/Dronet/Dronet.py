#!/usr/bin/env python
import rospy
from dronet_tello.msg import CNN_out
from sensor_msgs.msg import Image
from std_msgs.msg import Bool, Empty
import utils

from keras import backend as K

TEST_PHASE = 0


class Dronet(object):
    def __init__(
        self,
        json_model_path,
        weights_path,
        target_size=(200, 200),
        crop_size=(150, 150),
        imgs_rootpath="../models",
    ):

        self.pub = rospy.Publisher("/cnn_out/predictions", CNN_out, queue_size=5)
        # self.feedthrough_sub = rospy.Subscriber(
        #     "state_change", Bool, self.callback_feedthrough, queue_size=1
        # )
        # self.land_sub = rospy.Subscriber(
        #     "land", Empty, self.callback_land, queue_size=1
        # )
        self.image_sub = rospy.Subscriber(
            "/image_raw", Image, self.image_callback, queue_size=1
        )

        self.use_network_out = True
        self.imgs_rootpath = imgs_rootpath

        # Set keras utils
        K.set_learning_phase(TEST_PHASE)

        # Load json and create model
        model = utils.jsonToModel(json_model_path)
        # Load weights
        model.load_weights(weights_path)
        print("Loaded model from {}".format(weights_path))

        model.compile(loss="mse", optimizer="sgd")
        self.model = model
        self.target_size = target_size
        self.crop_size = crop_size
        self.data = None
        self.rate = rospy.Rate(10)

    # def callback_feedthrough(self, data):
    #     self.use_network_out = data.data

    # def callback_land(self, data):
    #     self.use_network_out = False

    def image_callback(self, data):
        self.data = data

    def run(self):
        while not rospy.is_shutdown():
            if self.data is None:
                continue
            msg = CNN_out()
            msg.header.stamp = rospy.Time.now()
            # data = None
            # while data is None:
            # try:
            #     data = rospy.wait_for_message("/image_raw", Image, timeout=5)
            # except:
            #     rospy.logwarn("DNN is not receiving messages")
            #     continue

            # if self.use_network_out:
            #     print("Publishing commands!")
            # else:
            #     print("NOT Publishing commands!")

            rospy.loginfo("Received image!")
            cv_image = utils.callback_img(
                self.data,
                self.target_size,
                self.crop_size,
                self.imgs_rootpath,
                self.use_network_out,
            )
            outs = self.model.predict_on_batch(cv_image[None])
            rospy.loginfo("Predicted values: %s", outs)
            steer, coll = outs[0][0], outs[1][0]
            msg.steering_angle = steer
            msg.collision_prob = coll
            # if self.use_network_out:
            #     print(msg)
            self.pub.publish(msg)
            self.data = None
            # self.rate.sleep()
