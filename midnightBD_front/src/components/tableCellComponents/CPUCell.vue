<template>
  <div v-if="modelType == 'intel'" class="text-intelblue min-w-16">
    <!--<img src="../icons/INTEL.svg" alt="Intel Icon" class="size-4" />-->
    {{ strToDisplay }}
  </div>
  <div v-else-if="modelType == 'amd'" class="text-amdred min-w-16">
    <!--<img src="../icons/AMD.svg" alt="AMD Icon" />-->
    R{{ strToDisplay }}
  </div>
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
      let match = this.display_value.match(/intel (\w*) ((\w| |\-)*)/i);
      if (match) {
        this.modelType = "intel";
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
  mounted() {
    this.setModelType();
  },
};
</script>

<style>
.text-intelblue {
  color: #0068b5;
}
.text-amdred {
  color: #ed1c24;
}
</style>
