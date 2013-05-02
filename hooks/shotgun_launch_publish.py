"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------

Hook for launching the app for a publish.

This hook typically looks at the extension of the input file
and based on this determine which launcher app to dispatch
the request to.

If no suitable launcher is found, return False, and the app
will launch the file in default viewer.
"""

from tank import Hook
from tank import TankError
import os

class LaunchAssociatedApp(Hook):
    
    def _create_folders(self, engine, entity):
        """
        Helper method. Creates folders if an entity is specified.
        """
        if entity:
            self.parent.tank.create_filesystem_structure(entity["type"], entity["id"], engine)                
    
    def execute(self, path, context, associated_entity, **kwargs):

        engine = self.parent.engine
        status = False

        ########################################################################
        # Example implementation below:

        if path.endswith(".nk"):
            # nuke
            if "tk-shotgun-launchnuke" in engine.apps:
                # looks like there is a nuke launcher installed in this system!
                self._create_folders("tk-nuke", associated_entity)
                status = True
                engine.apps["tk-shotgun-launchnuke"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launchnuke app could not be found in the environment")

        elif path.endswith(".ma") or path.endswith(".mb"):
            # maya
            if "tk-shotgun-launchmaya" in engine.apps:
                # looks like there is a maya launcher installed in this system!
                self._create_folders("tk-maya", associated_entity)
                status = True
                engine.apps["tk-shotgun-launchmaya"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launchmaya app could not be found in the environment")

        elif path.endswith(".fbx"):
            # Motionbuilder
            if "tk-shotgun-launchmotionbuilder" in engine.apps:
                # looks like there is a maya launcher installed in this system!
                self._create_folders("tk-motionbuilder", associated_entity)
                status = True
                engine.apps["tk-shotgun-launchmotionbuilder"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launchmotionbuilder app could not be found in the environment")
            
        elif path.endswith(".hrx"):
            # Hiero
            if "tk-shotgun-launchhiero" in engine.apps:
                # looks like there is a maya launcher installed in this system!
                self._create_folders("tk-hiero", associated_entity)
                status = True
                engine.apps["tk-shotgun-launchhiero"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launchhiero app could not be found in the environment")
            
        elif path.endswith(".max"):
            # 3ds Max
            if "tk-shotgun-launch3dsmax" in engine.apps:
                # looks like there is a maya launcher installed in this system!
                self._create_folders("tk-3dsmax", associated_entity)
                status = True
                engine.apps["tk-shotgun-launch3dsmax"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launch3dsmax app could not be found in the environment")
            
        elif path.endswith(".psd"):
            # Photoshop
            if "tk-shotgun-launchphotoshop" in engine.apps:
                self._create_folders("tk-photoshop", associated_entity)
                status = True
                engine.apps["tk-shotgun-launchphotoshop"].launch_from_path(path)
            else:
                raise TankError("the tk-shotgun-launchphotoshop app could not be found in the environment")

        return status
