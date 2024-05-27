<template>
  <p v-if="modelType == 'nvidia'" class="text-nvidiagreen">
    <!--<img src="../icons/INTEL.svg" alt="Intel Icon" class="size-4" />-->
    {{ strToDisplay }}
  </p>
  <p v-else-if="modelType == 'amd'" class="text-amdred">
    <!--<img src="../icons/AMD.svg" alt="AMD Icon" />-->
    {{ strToDisplay }}
  </p>
</template>

<script>
export default {
  name: "CPUCell",
  props: ["display_value"],
  data() {
    return {
      modelType: "",
      strToDisplay: "",
    };
  },
  methods: {
    setModelType() {
      let match = this.display_value.match(/nvidia (\w*) ((\w| |\-)*)/i);
      if (match) {
        this.modelType = "nvidia";
        this.strToDisplay = match[2];
        return;
      }
      match = this.display_value.match(/amd (\w*) ((\w| |\-)*)/i);
      if (match) {
        this.modelType = "amd";
        this.strToDisplay = match[2];
        return;
      }
    },
  },
  watch: {
    display_value(newVal, oldVal) {
      this.setModelType();
    },
  },
};
</script>

<style>
.text-nvidiagreen {
  color: #76B900;
}
.text-amdred {
  color: #ed1c24;
}
</style>
