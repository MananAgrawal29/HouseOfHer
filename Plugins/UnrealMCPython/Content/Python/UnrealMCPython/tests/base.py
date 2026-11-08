import unittest
import importlib
import json
import unreal

TEST_ROOT = "/Game/Tests/MCP"


class MCPTestCase(unittest.TestCase):

    def call(self, module_name, func_name, **kwargs):
        mod = importlib.import_module(f"UnrealMCPython.{module_name}")
        importlib.reload(mod)
        return json.loads(getattr(mod, func_name)(**kwargs))

    def assertSuccess(self, result, msg=None):
        self.assertTrue(result.get("success"), msg or f"Expected success=True: {result}")

    def delete_asset(self, path):
        try:
            if unreal.EditorAssetLibrary.does_asset_exist(path):
                unreal.EditorAssetLibrary.delete_asset(path)
        except Exception:
            pass

    def delete_actor_by_label(self, label):
        try:
            sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            for actor in sub.get_all_level_actors():
                if actor.get_actor_label() == label:
                    sub.destroy_actor(actor)
                    break
        except Exception:
            pass

    def ensure_test_dir(self):
        unreal.EditorAssetLibrary.make_directory(TEST_ROOT)
