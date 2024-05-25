<template>
  <div class="card w-full flex">
    <Button
      label="Новый Клиент"
      @click="client_overlay_visible = true"
      class="mx-3 grow"
    />
    <OverlayCreateClient v-model:visible="client_overlay_visible" />

    <Button
      label="Новая Сборка"
      @click="build_overlay_visible = true"
      class="mx-3 grow"
    />
    <OverlayCreateBuild v-model:visible="build_overlay_visible" />
  </div>
</template>

<script>
import Button from "primevue/button";
import OverlayCreateClient from "./OverlayCreateClient.vue";
import OverlayCreateBuild from "./OverlayCreateBuild.vue";

export default {
  name: "ControlPanel",
  components: {
    OverlayCreateClient,
    OverlayCreateBuild,
    Button,
  },
  data() {
    return {
      client_overlay_visible: false,
      build_overlay_visible: false,
    };
  },
};
</script>
