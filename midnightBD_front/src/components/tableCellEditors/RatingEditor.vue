<template>
  <Rating v-model="rating" :cancel="false" />
</template>

<script>
import Rating from "primevue/rating";

export default {
  name: "RatingCell",
  props: ["display_value"],
  data() {
    return {
      rating: null,
    };
  },
  components: {
    Rating,
  },
  mounted() {
    this.rating = this.display_value;
  },
  watch: {
    rating(newVal, oldVal) {
      this.$emit("update_row", "rating", newVal);
    },
  },
};
</script>
