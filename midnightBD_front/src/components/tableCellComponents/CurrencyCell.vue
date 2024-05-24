<template>
  <p class="table__currency-text">{{ display_value }} ₽</p>
</template>

<script>
export default {
  name: "CurrencyCell",
  props: ["display_value"],
};
</script>
