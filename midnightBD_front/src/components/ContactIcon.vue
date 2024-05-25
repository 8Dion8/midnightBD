<template>
  <i :class="['pi', iconName]" style="font-size: 1.5rem"></i>
</template>

<script>
export default {
  props: {
    iconName: {
      type: String,
    },
  },
};
</script>

<style></style>
