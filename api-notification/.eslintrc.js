module.exports = {
  env: {
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier/@typescript-eslint',
    'plugin:prettier/recommended',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint', 'simple-import-sort'],
  rules: {
    'simple-import-sort/imports': 'error',
    'prettier/prettier': ['error', { singleQuote: true }],
    '@typescript-eslint/explicit-module-boundary-types': 0,
    'spaced-comment': ['error', 'always'],
    'eol-last': ['error', 'always'],
    'max-len': [
      'error',
      {
        code: 140,
        tabWidth: 2,
        ignoreComments: true,
        ignoreTrailingComments: true,
        ignoreUrls: true,
        ignoreTemplateLiterals: true,
        ignoreRegExpLiterals: true,
      },
    ],
    'no-console': ['error', { allow: ['warn', 'error'] }],
    'no-trailing-spaces': 'error',
    'no-undef-init': 'error',
    'no-unused-expressions': 'error',
    'no-var': 'error',
    'sort-keys': 'off',
    'prefer-const': 'error',
    quotemark: ['off', 'single'],
    radix: 'error',
    semi: ['error', 'always'],
    eqeqeq: ['error', 'always', { null: 'ignore' }],
    'valid-typeof': 'error',
    'variable-name': 'off',
    'comma-dangle': ['error', 'always-multiline'],
    '@typescript-eslint/no-unused-vars': 'off',
    '@typescript-eslint/no-unused-vars-experimental': 'off',
    'no-case-declarations': 'off',
  },
};