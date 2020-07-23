Pythonista UI constraints driven by the Key Value Observing (KVO) protocol

## History

[First version](https://github.com/mikaelho/pythonista-uiconstraints) of UI constraints for Pythonista were created as a wrapper around Apple [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint?language=objc) class. While functional, it suffered from the same restrictions as the underlying Apple class, and was somewhat inconvenient to develop with, due to the "either frames or constraints" mindset and some mystical crashes.

[Second version]() was built on top of the [scripter](https://github.com/mikaelho/scripter), utilizing the `ui.View` `update` method that gets called several times a second. Constraints could now be designed freely, and this version acted as an excellent proof of concept. There was the obvious performance concern due to the constraints being checked constantly, even if nothing was happening in the UI – easily few thousand small checks per second for a realistic UI.

This version replaces the `update` method with the [KVO](https://developer.apple.com/documentation/objectivec/nsobject/nskeyvalueobserving?language=objc) (Key Value Observing) protocol, running the constraint checks only when the position or the frame of the view changes. Thus we avoid the performance overhead while retaining the freedom of custom constraints.
