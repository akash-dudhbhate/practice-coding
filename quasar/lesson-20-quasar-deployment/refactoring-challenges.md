# Lesson 20 — Refactoring Challenges

## Refactor 01 (Easy): Wrong Build Mode
### Before
```bash
quasar build
```
### After
```bash
quasar build -m pwa
```

## Refactor 02 (Medium): No .env.production
### Before
```bash
quasar build  # uses dev env vars
```
### After
```bash
# create .env.production
quasar build
```

## Refactor 03 (Hard: Manual Deploy
### Before
```bash
quasar build && scp dist/spa/* server:
```
### After
```yaml
# CI/CD pipeline
- run: quasar build -m spa
- uses: deploy-action
```
