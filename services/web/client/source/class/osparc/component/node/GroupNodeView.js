/* ************************************************************************

   osparc - the simcore frontend

   https://osparc.io

   Copyright:
     2020 IT'IS Foundation, https://itis.swiss

   License:
     MIT: https://opensource.org/licenses/MIT

   Authors:
     * Odei Maiz (odeimaiz)

************************************************************************ */

/**
 *
 * *Example*
 *
 * Here is a little example of how to use the widget.
 *
 * <pre class='javascript'>
 *   let groupNodeView = new osparc.component.node.GroupNodeView();
 *   groupNodeView.setNode(workbench.getNode1());
 *   groupNodeView.populateLayout();
 *   this.getRoot().add(groupNodeView);
 * </pre>
 */

qx.Class.define("osparc.component.node.GroupNodeView", {
  extend: osparc.component.node.BaseNodeView,

  construct: function() {
    this.base(arguments);
  },

  statics: {
    getSettingsEditorLayout: function(nodes) {
      const settingsEditorLayout = osparc.component.node.BaseNodeView.createSettingsGroupBox("Settings");
      Object.values(nodes).forEach(innerNode => {
        const propsWidgetEditor = innerNode.getPropsWidgetEditor();
        if (propsWidgetEditor && Object.keys(innerNode.getInputs()).length) {
          const innerSettings = osparc.component.node.BaseNodeView.createSettingsGroupBox().set({
            maxWidth: 700
          });
          innerNode.bind("label", innerSettings, "legend");
          innerSettings.add(propsWidgetEditor);
          settingsEditorLayout.add(innerSettings);
        }
      });
      return settingsEditorLayout;
    }
  },

  members: {
    _addSettings: function() {
      this._settingsLayout.removeAll();
      this._mapperLayout.removeAll();

      const innerNodes = this.getNode().getInnerNodes(true);
      Object.values(innerNodes).forEach(innerNode => {
        const propsWidget = innerNode.getPropsWidget();
        if (propsWidget && Object.keys(innerNode.getInputs()).length && propsWidget.hasVisibleInputs()) {
          const innerSettings = osparc.component.node.BaseNodeView.createSettingsGroupBox();
          innerNode.bind("label", innerSettings, "legend");
          innerSettings.add(propsWidget);
          this._settingsLayout.add(innerSettings);
        }
        const mapper = innerNode.getInputsMapper();
        if (mapper) {
          this._mapperLayout.add(mapper, {
            flex: 1
          });
        }
      });

      this._addToMainView(this._settingsLayout);
      this._addToMainView(this._mapperLayout, {
        flex: 1
      });
    },

    isSettingsGroupShowable: function() {
      let anyVisible = false;
      const innerNodes = this.getNode().getInnerNodes(true);
      const innerNodesArray = Object.values(innerNodes);
      for (let i=0; i<innerNodesArray.length && !anyVisible; i++) {
        const innerNode = innerNodesArray[i];
        const propsWidget = innerNode.getPropsWidget();
        if (propsWidget) {
          anyVisible = propsWidget.hasVisibleInputs();
        } else {
          anyVisible = false;
        }
      }
      return anyVisible;
    },

    __iFrameChanged: function(innerNode, tabPage) {
      const loadingPage = innerNode.getLoadingPage();
      const iFrame = innerNode.getIFrame();

      tabPage.removeAll();
      const src = iFrame.getSource();
      if (src === null || src === "about:blank") {
        tabPage.add(loadingPage);
      } else {
        tabPage.add(iFrame);
      }
    },

    _addIFrame: function() {
      this._iFrameLayout.removeAll();

      const tabView = new qx.ui.tabview.TabView().set({
        contentPadding: 0
      });
      const innerNodes = this.getNode().getInnerNodes(true);
      Object.values(innerNodes).forEach(innerNode => {
        const loadingPage = innerNode.getLoadingPage();
        const iFrame = innerNode.getIFrame();
        if (loadingPage === null && iFrame === null) {
          return;
        }
        [
          loadingPage,
          iFrame
        ].forEach(widget => {
          if (widget) {
            widget.addListener("maximize", e => {
              this._maximizeIFrame(true);
            }, this);
            widget.addListener("restore", e => {
              this._maximizeIFrame(false);
            }, this);
            this._maximizeIFrame(widget.hasState("maximized"));
          }
        });

        const page = new qx.ui.tabview.Page().set({
          layout: new qx.ui.layout.Grow(),
          showCloseButton: false
        });
        innerNode.bind("label", page, "label");
        tabView.add(page);

        this.__iFrameChanged(innerNode, page);

        iFrame.addListener("load", () => {
          this.__iFrameChanged(innerNode, page);
        });
      });

      if (tabView.getChildren()) {
        this._iFrameLayout.add(tabView, {
          flex: 1
        });

        this._addToMainView(this._iFrameLayout, {
          flex: 1
        });
      }
    },

    _openEditAccessLevel: function() {
      const settingsEditorLayout = this.self().getSettingsEditorLayout(this.getNode().getInnerNodes());
      const win = osparc.component.node.BaseNodeView.createWindow(this.getNode().getLabel());
      win.add(settingsEditorLayout);
      win.center();
      win.open();
    },

    _applyNode: function(node) {
      if (!node.isContainer()) {
        console.error("Only group nodes are supported");
      }
    }
  }
});
