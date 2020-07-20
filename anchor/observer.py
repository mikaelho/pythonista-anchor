import objc_util

import anchor.objc_plus as objc_plus


class NSKeyValueObserving(objc_plus.ObjCDelegate):
    
    def __init__(self, observer_attribute='observer'):        
        #objc_util.retain_global(self)
        self.targets = {}
        self.observerattr = observer_attribute
        self.observeattrs = (
            'bounds',
            'transform',
            'position',
            'anchorPoint',
            'frame')
    
    def observe(self, target):
        objc_target = target.objc_instance
        if objc_target in self.targets: return
        self.targets[objc_target] = target
        for key in self.observeattrs:
            objc_target.layer().addObserver_forKeyPath_options_context_(
                self, key, 0, None)
        
                
    def stop_observing(self, target):
        objc_target = target.objc_instance
        target_view = self.targets.pop(objc_target, None)
        if target_view:
            for key in self.observeattrs:
                objc_target.layer().\
                removeObserver_forKeyPath_(self, key)
            
    def stop_all(self):
        for target in list(self.targets.values()):
            self.stop_observing(target)
    
    def observeValueForKeyPath_ofObject_change_context_(
        _self, _cmd, _path, _obj, _change, _ctx
    ):
        self = objc_util.ObjCInstance(_self)
        objc_target = objc_util.ObjCInstance(_obj).delegate()
        try:
            target = self.targets[objc_target]
            getattr(target, self.observerattr).on_change()
        except Exception as e:
            print('observeValueForKeyPath:', self, type(e), e)


