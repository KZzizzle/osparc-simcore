qx.Class.define("qxapp.data.model.ProjectModel", {
  extend: qx.core.Object,

  construct: function(prjData, fromTemplate) {
    this.base(arguments);

    if (prjData) {
      this.set({
        uuid: fromTemplate ? qxapp.utils.Utils.uuidv4() : prjData.projectUuid || this.getUuid(),
        name: prjData.name || this.getName(),
        description: prjData.description || this.getDescription(),
        notes: prjData.notes || this.getNotes(),
        thumbnail: prjData.thumbnail || this.getThumbnail(),
        owner: prjData.owner || this.getOwner(),
        collaborators: prjData.collaborators || this.getCollaborators(),
        creationDate: new Date(prjData.creationDate) || this.getCreationDate(),
        lastChangeDate: new Date(prjData.lastChangeDate) || this.getLastChangeDate()
      });
    }

    if (prjData && prjData.workbench) {
      this.setWorkbenchModel(new qxapp.data.model.WorkbenchModel(this.getName(), prjData.workbench));
    } else {
      this.setWorkbenchModel(new qxapp.data.model.WorkbenchModel(this.getName(), {}));
    }
  },

  properties: {
    uuid: {
      check: "String",
      nullable: false,
      init: qxapp.utils.Utils.uuidv4()
    },

    name: {
      check: "String",
      nullable: false,
      init: "New Project",
      apply : "__applyName"
    },

    description: {
      check: "String",
      nullable: true,
      init: "Empty"
    },

    notes: {
      check: "String",
      nullable: true,
      init: "Empty"
    },

    thumbnail: {
      check: "String",
      nullable: true,
      init: "https://imgplaceholder.com/171x96/cccccc/757575/ion-plus-round"
    },

    owner: {
      check: "String",
      nullable: true,
      init: ""
    },

    collaborators: {
      check: "Object",
      nullable: true,
      init: {}
    },

    creationDate: {
      check: "Date",
      nullable: true,
      init: new Date()
    },

    lastChangeDate: {
      check: "Date",
      nullable: true,
      init: new Date()
    },

    workbenchModel: {
      check: "qxapp.data.model.WorkbenchModel",
      nullable: false
    }
  },

  members: {
    __applyName: function(newName) {
      if (this.isPropertyInitialized("workbenchModel")) {
        this.getWorkbenchModel().setProjectName(newName);
      }
    },

    serializeProject: function() {
      this.setLastChangeDate(new Date());

      let jsonObject = {};
      let properties = this.constructor.$$properties;
      for (let key in properties) {
        if (key === "workbenchModel") {
          jsonObject["workbench"] = this.getWorkbenchModel().serializeWorkbench();
        } else {
          jsonObject[key] = this.get(key);
        }
      }
      return jsonObject;
    }
  }
});