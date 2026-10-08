# 33 — `abstract class` vs `interface` — when to use each

> **Interview question:** "When would you use an abstract class instead of an interface in TypeScript?"
> **What the interviewer is really testing:** Whether you understand the real difference isn't "has code vs no code" — it's that an abstract class is a *runtime artifact* (a real constructor, `extends`-only, template methods) while an interface is a *pure contract* that vanishes at compile time (and can be `implements`-ed many-at-once, extended by anything, declaration-merged).

## Theory — what it is

Both describe "what a thing must have," but they live in different worlds:

```typescript
interface Shape {                    // contract only — erased at compile
  area(): number;
}

abstract class Animal {              // contract + real runtime class
  constructor(public name: string) {}
  abstract speak(): string;          // subclass MUST implement
  describe(): string {               // shared implementation
    return `${this.name} says ${this.speak()}`;
  }
}
```

Rules that matter:

- **Interface = shape, nothing more.** No code, no constructor, no runtime existence — `x instanceof SomeInterface` is a compile error because the interface doesn't exist in the emitted JS.
- **Abstract class = real class you can't `new`.** `new Animal()` is a compile error — it exists only to be `extends`-ed. It can mix abstract members (subclass must fill in) with concrete members (shared code) — the **template method pattern**: `describe()` above calls the abstract `speak()`, so the parent controls the algorithm skeleton while subclasses supply the steps.
- **Inheritance arithmetic:** a class `extends` exactly **one** class (abstract or not) but can `implements` **many** interfaces — `class C implements A, B`.
- **Interfaces can describe anything:** objects, functions, arrays — `interface Fn { (x: number): string }`. Abstract classes only describe class instances.
- **Interfaces merge; classes don't.** Two `interface Foo` declarations in the same scope merge their members (declaration merging — how library types get extended). Class declarations collide instead.
- **Both can be `implements`-ed:** `class Dog implements Serializable` and `class Dog extends Animal` — but `implements` on a class ignores its code and just checks its shape.

## Why it was needed

Interfaces exist because JavaScript has no static contract system — you needed a way to say "anything passed here must have `.save()`" without dictating *how* the object is built (class, literal, factory, mock). They answer "what can it do?"

Abstract classes exist because OO code needs the opposite half: "how does it work, except for these pieces I can't know yet?" Before abstract classes, you'd write a normal base class and document "don't instantiate this" — the compiler now enforces it, and `abstract` methods force subclasses to fill in the gaps rather than silently inheriting a broken default.

## Where it's used in a real project

- **Interface — dependency boundaries:** `interface UserRepo { findById(id): Promise<User> }` — services depend on the contract; production uses `PostgresUserRepo`, tests use `InMemoryUserRepo`. Mocking needs no inheritance.
- **Interface — API payloads/configs:** `interface CreateUserDto`, `interface AppConfig` — pure data shapes.
- **Abstract class — template method:** `abstract class BaseController` with concrete `handleRequest()` that calls abstract `validate()`/`execute()` — NestJS/Angular-style base classes.
- **Abstract class — shared state + contract:** `abstract class Connection` holding `status`, `reconnect()` logic, forcing subclasses to implement `send()`.
- **`instanceof` checks:** only classes (abstract included) work with `instanceof` — a real reason to pick an abstract class when you need runtime discrimination.

## Diagram

```
INTERFACE — pure contract, erased at compile
  interface Logger { log(msg: string): void }

  class ConsoleLogger implements Logger {...}   ┐
  class FileLogger    implements Logger {...}   ├── many implements OK
  const mock: Logger = { log: () => {} };       ┘   even object literals fit

  Emitted JS: NOTHING — interface is gone.
  x instanceof Logger   -> ❌ compile error


ABSTRACT CLASS — real class, one single parent
  abstract class Repo {
    protected cache = new Map();           // shared state
    find(id: string) {                     // template method (concrete)
      return this.cache.get(id) ?? this.load(id);
    }
    protected abstract load(id: string): unknown;  // subclass must fill
  }

  new Repo()              -> ❌ compile error (can't instantiate)
  class UserRepo extends Repo implements Serializable {
    load(id) {...}        // must implement, or class won't compile
  }

  extends: ONE class only ──► but it gives real code, state,
                              constructor, and instanceof Repo ✅
```

## Code — explained

```typescript
// 1. Interface — a promise about shape, nothing else
interface Notifier {
  send(to: string, msg: string): void;
}

// 2. Anything with that shape fits — class, literal, mock
const fakeNotifier: Notifier = { send: () => {} };   // perfect for tests

// 3. Abstract class — contract + shared machinery
abstract class BaseNotifier implements Notifier {
  constructor(protected retries: number) {}      // real constructor

  abstract send(to: string, msg: string): void;  // subclass MUST provide

  notify(to: string, msg: string): void {        // template method
    for (let i = 0; i <= this.retries; i++) {
      try {
        this.send(to, msg);                       // calls the abstract hook
        console.log(`sent to ${to}`);
        return;
      } catch { /* retry */ }
    }
  }
}

// 4. Concrete subclass — fills in the abstract part
class EmailNotifier extends BaseNotifier {
  send(to: string, msg: string): void {
    console.log(`email -> ${to}: ${msg}`);
  }
}

const n: Notifier = new EmailNotifier(3);          // (5) typed as contract
n.send("ana@x.com", "hi");                          // direct call
// new BaseNotifier(1);                             // (6) Error: abstract!
// n instanceof Notifier;                           // (7) Error: type gone
console.log(n instanceof BaseNotifier);             // (8) true — class exists

// 9. Interfaces do what classes can't: multiple + merging
interface A { a(): void }
interface B { b(): void }
class Both implements A, B {
  a() { console.log("a"); }
  b() { console.log("b"); }
}
new Both().a();                                     // a
```

1. `Notifier` is a pure shape — after compile it disappears entirely.
2. An object literal satisfies it without any class — that's why interfaces are the test-double tool.
3. `BaseNotifier implements Notifier` — the abstract class *also* promises the interface's contract, plus adds a real constructor and shared code.
4. `EmailNotifier` must implement `send` — leave it out and the class itself errors (`Non-abstract class 'EmailNotifier' does not implement...`).
5. `const n: Notifier` — depend on the contract, not the concrete class; swapping `EmailNotifier` for `SmsNotifier` is a one-line change.
6. `new BaseNotifier()` — the whole point of `abstract`: a half-built machine can't be instantiated.
7. `instanceof` needs a runtime value — interfaces are erased, so this is a compile error.
8. But `BaseNotifier` *is* a real class at runtime — `instanceof` works. This is often the tiebreaker for choosing abstract class over interface.
9. Multiple `implements` — no class can do this with `extends`.

## Problems

### Easy — implement an interface two ways
**Problem:** Define `interface Greeter { greet(name: string): string }`. Make a class that implements it AND a plain object that satisfies it — prove both work through the interface type.
**Try this input:** call `greet("Ana")` on both.
**Expected output:** `Hello, Ana` logged twice.
**Solution:**
```typescript
interface Greeter {
  greet(name: string): string;
}

class FriendlyGreeter implements Greeter {
  greet(name: string): string {
    return `Hello, ${name}`;
  }
}

const literalGreeter: Greeter = {
  greet: (name) => `Hello, ${name}`,
};

const greetAll = (g: Greeter) => console.log(g.greet("Ana"));
greetAll(new FriendlyGreeter());   // Hello, Ana
greetAll(literalGreeter);          // Hello, Ana — no class needed
```
**Logic explained:**
1. `implements Greeter` makes the compiler verify `FriendlyGreeter` has `greet` — remove the method and the *class declaration* errors.
2. The object literal needs no `implements` — TypeScript checks structurally: has `greet` with the right signature? Then it's a `Greeter`.
3. `greetAll` depends only on the interface — it can't tell or care which of the two it received.

### Medium — template method pattern
**Problem:** Build `abstract class Importer` where `import(file)` (concrete) calls abstract `parse(raw: string)` then concrete `save(parsed)`. Subclass `CsvImporter` implements `parse`. Show `import` running the fixed pipeline with the subclass's step.
**Try this input:** `new CsvImporter().import("a,b\nc,d")`.
**Expected output:**
```
parsed: [ [ 'a', 'b' ], [ 'c', 'd' ] ]
saved 2 rows
```
**Solution:**
```typescript
abstract class Importer {
  import(raw: string): void {
    const rows = this.parse(raw);       // hook — subclass supplies
    this.save(rows);                    // shared step
  }
  protected abstract parse(raw: string): string[][];
  protected save(rows: string[][]): void {
    console.log(`saved ${rows.length} rows`);
  }
}

class CsvImporter extends Importer {
  protected parse(raw: string): string[][] {
    const rows = raw.split("\n").map((l) => l.split(","));
    console.log("parsed:", rows);
    return rows;
  }
}

new CsvImporter().import("a,b\nc,d");
// parsed: [ [ 'a', 'b' ], [ 'c', 'd' ] ]
// saved 2 rows
```
**Logic explained:**
1. `import` is the *template*: fixed order (parse → save), with `parse` left abstract because the base can't know the format.
2. `parse` is `protected abstract` — callable inside the class, invisible outside, required in subclasses.
3. `save` is concrete and inherited — the point of the abstract class: shared code ships with the contract.
4. An interface couldn't do this — it can say "must have `parse`" but can't *contain* the `import` pipeline that calls it.

### Hard — interface for the boundary, abstract for the machinery
**Problem:** Design a retryable job system: `interface Job { run(): Promise<void> }` is the public contract; `abstract class RetryableJob` implements it, providing concrete `run()` that retries abstract `attempt()` up to N times. Show a `SyncJob` failing once then succeeding.
**Try this input:** `await new SyncJob(2).run()` where `attempt` fails on first call.
**Expected output:**
```
attempt 1 failed, retrying
done on attempt 2
```
**Solution:**
```typescript
interface Job {
  run(): Promise<void>;
}

abstract class RetryableJob implements Job {
  constructor(private maxRetries: number) {}

  async run(): Promise<void> {                    // concrete pipeline
    for (let i = 1; i <= this.maxRetries + 1; i++) {
      try {
        await this.attempt(i);                    // abstract hook
        return;
      } catch {
        if (i <= this.maxRetries) {
          console.log(`attempt ${i} failed, retrying`);
        } else {
          throw new Error("all retries failed");
        }
      }
    }
  }

  protected abstract attempt(n: number): Promise<void>;
}

class SyncJob extends RetryableJob {
  private calls = 0;
  protected async attempt(n: number): Promise<void> {
    this.calls++;
    if (this.calls < 2) throw new Error("flaky");
    console.log(`done on attempt ${n}`);
  }
}

async function main() {
  await new SyncJob(2).run();
  // attempt 1 failed, retrying
  // done on attempt 2
}
main();
```
**Logic explained:**
1. `Job` is the boundary — schedulers, queues, and mocks only know `run()`.
2. `RetryableJob` is machinery: it *implements* `Job` by providing `run` (the retry loop) and delegating the actual work to abstract `attempt` — contract and algorithm skeleton in one place.
3. `SyncJob` only writes the piece that's genuinely variable — what one attempt does. The retry policy is inherited, tested once, and shared.
4. Why not just an interface? Because `run`'s retry logic would be copy-pasted into every job. Why not just a class? Because consumers should still depend on the `Job` interface — `function schedule(j: Job)` accepts non-retryable jobs too.

## The 30-second interview answer

"An interface is a pure contract — 'must have these members' — erased at compile time, so no `instanceof`, no code, no constructor. Anything with the right shape satisfies it: classes, object literals, mocks — and a class can implement many interfaces. An abstract class is a real class you can't `new`: it can carry state, constructors, and shared concrete methods, and it can declare `abstract` members that subclasses are forced to fill in — the template method pattern, where the base controls the pipeline and subclasses supply the steps. The tradeoffs: `extends` is single-inheritance while `implements` is unlimited; interfaces merge via declaration merging and can describe functions/objects, classes can't. I reach for an interface at dependency boundaries — services, repos, anything I want to mock — and an abstract class when subclasses genuinely share code or I need `instanceof` at runtime."

## Follow-up trap

**"Can a class implement an abstract class — i.e. `class X implements BaseAbstract`?"** — Yes, and it's surprising: `implements` treats the class as its *instance-side shape* — it checks X has the same members but ignores all of Base's code and gives X no inheritance. It's legal but rarely what you want; `extends` is usually meant. Second trap: **"since interfaces are erased, how do you check at runtime that something satisfies an interface?"** — You can't `instanceof` it; you write a type guard (`x is Notifier` checking `typeof x.send === "function"`) or use a discriminated-union tag. If runtime discrimination is a hard requirement, that's a point for a base class. Third: **"abstract methods vs methods that throw `new Error('implement me')`?"** — the throwing version compiles fine and blows up at *runtime*; `abstract` makes the subclass's missing method a *compile* error, which is strictly better.
