<template>
    <Tag :value=display_value></Tag>
</template>

<script>
import Tag from 'primevue/tag';

export default {
    name: "TagCell",
    props: ['display_value'],
    components: {
        Tag
    }
}

</script>
