from UnrealMCPython.tests.base import MCPTestCase, TEST_ROOT

_BT_PATH = f"{TEST_ROOT}/MCP_TestBT"
_BB_PATH = f"{TEST_ROOT}/MCP_TestBB"


class TestBehaviorTreeActions(MCPTestCase):

    def setUp(self):
        self._bt_path = None
        self._bb_path = None
        self.ensure_test_dir()

        r = self.call("behavior_tree_actions", "ue_create_blackboard",
                      asset_path=_BB_PATH)
        if r.get("success"):
            self._bb_path = _BB_PATH

        r = self.call("behavior_tree_actions", "ue_create_behavior_tree",
                      asset_path=_BT_PATH)
        if r.get("success"):
            self._bt_path = _BT_PATH

    def tearDown(self):
        if self._bt_path:
            self.delete_asset(self._bt_path)
        if self._bb_path:
            self.delete_asset(self._bb_path)

    def _skip_if_no_bt(self):
        if not self._bt_path:
            self.skipTest("BehaviorTree not created in setUp")

    def _skip_if_no_bb(self):
        if not self._bb_path:
            self.skipTest("Blackboard not created in setUp")

    # ── list / read ───────────────────────────────────────────────────────────

    def test_list_behavior_trees(self):
        r = self.call("behavior_tree_actions", "ue_list_behavior_trees")
        self.assertSuccess(r)

    def test_list_bt_node_classes(self):
        r = self.call("behavior_tree_actions", "ue_list_bt_node_classes")
        self.assertSuccess(r)

    def test_get_behavior_tree_structure(self):
        self._skip_if_no_bt()
        # Build a minimal tree first so the BT is non-empty
        self.call("behavior_tree_actions", "ue_build_behavior_tree",
                  asset_path=self._bt_path,
                  tree_structure={"node_class": "BTComposite_Selector", "children": []})
        r = self.call("behavior_tree_actions", "ue_get_behavior_tree_structure",
                      asset_path=self._bt_path)
        self.assertSuccess(r)

    def test_get_blackboard_data(self):
        self._skip_if_no_bb()
        r = self.call("behavior_tree_actions", "ue_get_blackboard_data",
                      asset_path=self._bb_path)
        self.assertSuccess(r)

    # ── blackboard keys ───────────────────────────────────────────────────────

    def test_add_and_remove_blackboard_key(self):
        self._skip_if_no_bb()
        r = self.call("behavior_tree_actions", "ue_add_blackboard_key",
                      asset_path=self._bb_path,
                      key_name="TestFloat", key_type="Float")
        self.assertSuccess(r)

        r = self.call("behavior_tree_actions", "ue_remove_blackboard_key",
                      asset_path=self._bb_path, key_name="TestFloat")
        self.assertSuccess(r)

    def test_add_multiple_key_types(self):
        self._skip_if_no_bb()
        for key_type in ("Bool", "Int", "Vector", "String"):
            r = self.call("behavior_tree_actions", "ue_add_blackboard_key",
                          asset_path=self._bb_path,
                          key_name=f"Test_{key_type}", key_type=key_type)
            self.assertSuccess(r, f"Failed to add {key_type} key")

    # ── link ──────────────────────────────────────────────────────────────────

    def test_set_blackboard_to_behavior_tree(self):
        self._skip_if_no_bt()
        self._skip_if_no_bb()
        r = self.call("behavior_tree_actions", "ue_set_blackboard_to_behavior_tree",
                      bt_path=self._bt_path, bb_path=self._bb_path)
        self.assertSuccess(r)

    # ── build ─────────────────────────────────────────────────────────────────

    def test_build_behavior_tree(self):
        self._skip_if_no_bt()
        tree = {
            "node_class": "BTComposite_Selector",
            "children": [
                {"node_class": "BTTask_Wait", "properties": {"wait_time": 1.0}},
            ]
        }
        r = self.call("behavior_tree_actions", "ue_build_behavior_tree",
                      asset_path=self._bt_path, tree_structure=tree)
        self.assertSuccess(r)

    # ── node details / selection ────────────────────────────────────────────────

    def test_get_bt_node_details(self):
        self._skip_if_no_bt()
        # Build a tree, then read a node's details by its name from the structure.
        self.call("behavior_tree_actions", "ue_build_behavior_tree",
                  asset_path=self._bt_path,
                  tree_structure={"node_class": "BTComposite_Selector", "children": []})
        st = self.call("behavior_tree_actions", "ue_get_behavior_tree_structure",
                       asset_path=self._bt_path)
        self.assertSuccess(st)
        node_name = st["tree"][0]["node_name"]
        r = self.call("behavior_tree_actions", "ue_get_bt_node_details",
                      asset_path=self._bt_path, node_name=node_name)
        self.assertSuccess(r)

    def test_get_selected_bt_nodes(self):
        # No BT editor open in a headless test run → returns a structured failure.
        # We only assert the action runs end-to-end and returns a bool success.
        r = self.call("behavior_tree_actions", "ue_get_selected_bt_nodes")
        self.assertIsInstance(r.get("success"), bool)
