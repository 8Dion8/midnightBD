<template>
  <p>CPU{{ display_value }}</p>
</template>

<script>
export default {
  name: "CPUCell",
  props: ["display_value"],
};
</script>
