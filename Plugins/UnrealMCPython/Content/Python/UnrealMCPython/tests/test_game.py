from UnrealMCPython.tests.base import MCPTestCase, TEST_ROOT

_IA_PATH = f"{TEST_ROOT}/IA_TestJump"
_IMC_PATH = f"{TEST_ROOT}/IMC_TestDefault"


class TestGameActions(MCPTestCase):

    def setUp(self):
        self._ia_path = None
        self._imc_path = None
        self.ensure_test_dir()

    def tearDown(self):
        # Clear GameMode override
        self.call("game_actions", "ue_set_game_mode", game_mode_class_path=None)
        # Clean up created input assets
        if self._ia_path:
            self.delete_asset(self._ia_path)
        if self._imc_path:
            self.delete_asset(self._imc_path)

    # ── game mode ─────────────────────────────────────────────────────────────

    def test_clear_game_mode(self):
        r = self.call("game_actions", "ue_set_game_mode",
                      game_mode_class_path=None)
        self.assertSuccess(r)

    def test_set_game_mode_invalid_path(self):
        r = self.call("game_actions", "ue_set_game_mode",
                      game_mode_class_path="/Game/DoesNotExist/BP_FakeMode_C")
        self.assertFalse(r.get("success"))

    def test_set_game_mode_engine_class(self):
        r = self.call("game_actions", "ue_set_game_mode",
                      game_mode_class_path="/Script/Engine.GameModeBase")
        self.assertSuccess(r)

    # ── input action ──────────────────────────────────────────────────────────

    def test_add_input_action_bool(self):
        r = self.call("game_actions", "ue_add_input_action",
                      asset_path=_IA_PATH, value_type="Bool")
        self.assertSuccess(r)
        if r.get("success"):
            self._ia_path = _IA_PATH

    def test_add_input_action_axis2d(self):
        ia_path = f"{TEST_ROOT}/IA_TestLook"
        r = self.call("game_actions", "ue_add_input_action",
                      asset_path=ia_path, value_type="Axis2D")
        self.assertSuccess(r)
        if r.get("success"):
            self.delete_asset(ia_path)

    # ── input mapping ─────────────────────────────────────────────────────────

    def test_add_input_mapping(self):
        # Create the input action first
        r = self.call("game_actions", "ue_add_input_action",
                      asset_path=_IA_PATH, value_type="Bool")
        if r.get("success"):
            self._ia_path = _IA_PATH

        r = self.call("game_actions", "ue_add_input_mapping",
                      mapping_context_path=_IMC_PATH,
                      action_path=_IA_PATH,
                      key_name="SpaceBar")
        self.assertSuccess(r)
        if r.get("success"):
            self._imc_path = _IMC_PATH
