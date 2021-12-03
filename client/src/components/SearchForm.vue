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
          v-model="search_value"
          :label="`Enter ${textFieldLabel}`"
          outlined
          dense
        />
        <v-btn
          color="primary"
          :disabled="!valid"
          @click="search"
        >
          <v-icon>mdi-search</v-icon> Search
        </v-btn>
      </v-form>
      </v-col>
    </v-row>
    <v-row v-show="search_result" justify="center">
        <v-col cols="8">
            {{ search_result }}
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
import SearchService from '@/services/SearchService';

export default {
  name: 'SearchForm',
  data: () => ({
    search_type: "",
    search_value: "",
    search_types: [
      {
        text: 'NetId',
        value: 'netid'
      },
      {
        text: 'Email',
        value: 'mail'
      },
    ],
    search_result: null
  }),
  computed: {
    valid() {
      return !!this.search_type && !!this.search_value;
    },
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
  },
  methods: {
    async search() {
        this.search_result = await SearchService.get(this.search_type, this.search_value);
    }
  }
};
</script>
