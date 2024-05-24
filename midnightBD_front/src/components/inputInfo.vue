<template>
  <IconField iconPosition="left">
    <InputIcon :class="iconClass" />
    <InputText
      @input="updateInput($event.target.value)"
      :placeholder="placeholder"
    />
  </IconField>
</template>

<script>
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";
import InputText from "primevue/inputtext";

export default {
  name: "inputInfo",
  components: {
    IconField,
    InputText,
    InputIcon,
  },
  props: {
    iconClass: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      required: true,
    },
  },
  methods: {
    updateInput(val) {
      this.$emit("updateInput", val);
    },
  },
};
</script>
