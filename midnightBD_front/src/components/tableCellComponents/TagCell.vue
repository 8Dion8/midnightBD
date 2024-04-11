<template>
    <Tag :value=rowData[rowIndexToGet]></Tag>
</template>

<script>
import Tag from 'primevue/tag';

export default {
    name: "TagCell",
    props: ['rowData', 'rowIndexToGet'],
    components: {
        Tag
    }
}

</script>
