<template>
  <div class="card">
    <div class="flex flex-row space-x-4">
      <Menubar :model="items" class="grow h-min" />
    </div>
  </div>
</template>

<script>
import Menubar from "primevue/menubar";
import Card from "primevue/card";

export default {
  name: "Header",
  components: {
    Menubar,
    Card,
  },
  data() {
    return {
      user: "dion",
      items: [
        {
          label: "Сборки",
          icon: "pi pi-list-check",
          command: () => {
            this.switchTable("orders_build");
          },
        },
        {
          label: "Клиенты",
          icon: "pi pi-user",
          command: () => {
            this.switchTable("clients");
          },
        },
      ],
    };
  },
  props: {
    sql_table: {
      type: String,
    },
  },
  methods: {
    switchTable(table) {
      this.$emit("switchTable", table);
    },
  },
};
</script>

<style></style>
