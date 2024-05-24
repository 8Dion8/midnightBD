<template>
  <div class="card details-container">
    <h1 class="font-bold text-2xl">{{ this.data.name }}</h1>
  </div>
</template>

<script>
export default {
  name: "Details",

  data() {
    return {
      data: [],
      data_loaded: false,
    };
  },

  methods: {
    fetch_data() {
      if (this.sql_table == "clients") {
        fetch(
          `http://127.0.0.1:7900/clients/rows?column=id&filter=${this.selected_row_id}`
        )
          .then((response) => response.json())
          .then((rowData) => {
            console.log(rowData);
            this.data = rowData.data[0];
            this.data_loaded = true;
          })
          .catch((error) => {
            console.error("Error fetching row data:", error);
          });
      } else {
        fetch(
          `http://127.0.0.1:7900/${this.sql_table}/rows?column=id&filter=${this.selected_row_id}`
        )
          .then((response) => response.json())
          .then((rowData) => {
            console.log(rowData);
            let client_id = rowData.data[0].client;
            console.log(client_id);
            fetch(
              `http://127.0.0.1:7900/clients/rows?column=id&filter=${client_id}`
            )
              .then((response) => response.json())
              .then((rowData) => {
                console.log(rowData);
                this.data = rowData.data[0];
                this.data_loaded = true;
              })
              .catch((error) => {
                console.error("Error fetching row data:", error);
              });
          })
          .catch((error) => {
            console.error("Error fetching row data:", error);
          });
      }
    },
  },

  props: {
    selected_row_id: {
      type: Number,
    },
    sql_table: {
      type: String,
    },
  },

  watch: {
    selected_row_id(newID, oldID) {
      console.log("received", newID);
      this.fetch_data();
    },
  },
};
</script>
