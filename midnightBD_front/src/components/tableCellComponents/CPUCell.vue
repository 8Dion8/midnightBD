<template>
  <p v-if="modelType == 'intel'" class="text-intelblue">
    <!--<img src="../icons/INTEL.svg" alt="Intel Icon" class="size-4" />-->
    {{ strToDisplay }}
  </p>
  <p v-else-if="modelType == 'amd'" class="text-amdred">
    <!--<img src="../icons/AMD.svg" alt="AMD Icon" />-->
    R{{ strToDisplay }}
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
