
(cl:in-package :asdf)

(defsystem "dronet_tello-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CNN_out" :depends-on ("_package_CNN_out"))
    (:file "_package_CNN_out" :depends-on ("_package"))
    (:file "FlightData" :depends-on ("_package_FlightData"))
    (:file "_package_FlightData" :depends-on ("_package"))
  ))