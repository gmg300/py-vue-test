<template>
  <v-container>
    <v-row justify="center" >
      <v-col class="mt-4 search-form" cols="8">
      <v-form>
        <h2 color="primary">Find Northwestern Students, Faculty or Staff</h2>
        <v-select
          v-model="search_type"
          label="Search Type:"
          prefix="Search by"
          :items=search_types
          outlined
          dense
        />
        <v-text-field
          :label="`Enter ${textFieldLabel}`"
          outlined
          dense
        />
        <v-btn color="primary">
          <v-icon>mdi-search</v-icon> Search
        </v-btn>
      </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
  .search-form {
    border: 2px solid #4E2A84;
    background: #E4E0EE;
  }
  .v-text-field--outlined > .v-input__control > .v-input__slot {
    background: white;
  }
</style>

<script>
// import SearchService from '@/services/SearchService';

export default {
  name: 'SearchForm',
  data: () => ({
    search_type: "",
    search_types: [
      {
        text: 'NetId',
        value: 'netid'
      },
      {
        text: 'Email',
        value: 'mail'
      },
    ]
  }),
  computed: {
    textFieldLabel() {
      switch(this.search_type) {
        case 'netid':
          return 'NetId';
        case 'mail':
          return 'Email';
        default:
          return '...';
      }
    }
  }
};
</script>
