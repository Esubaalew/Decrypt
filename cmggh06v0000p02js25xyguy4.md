---
title: "Discover Run Kit: Your Versatile REPL and Command Line Tool for 25+ Languages"
seoTitle: "Explore Run Kit: Multi-Language REPL Tool"
seoDescription: "Run Kit facilitates coding in 25+ languages with a consistent CLI and REPL. Built in Rust for efficient, cross-platform development"
datePublished: Tue Oct 07 2025 11:22:28 GMT+0000 (Coordinated Universal Time)
cuid: cmggh06v0000p02js25xyguy4
slug: discover-run-kit-your-versatile-repl-and-command-line-tool-for-25-languages
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1759836109839/abc955b8-271c-41ba-aa68-f2e61fcc03a2.png
tags: opensource, cli, rust, rust-programming

---

[Website](https://run.esubalew.et/) • [Docs Overview](https://run.esubalew.et/docs/overview)

> Built in Rust for developers who live in multiple runtimes. `run` gives you a consistent CLI, persistent REPLs, and batteries-included examples for your favorite languages.

---

---

# Website and Docs

The official website and full documentation are available here:

* Website: [https://run.esubalew.et/](https://run.esubalew.et/)
    
* Docs Overview: [https://run.esubalew.et/docs/overview](https://run.esubalew.et/docs/overview)
    

Use these links to explore features, language guides, and detailed examples.

---

# Overview - Universal Multi-Language Runner

A powerful command-line tool for executing code in 25 programming languages

## What is run?

Run is a universal multi-language runner and smart REPL (Read-Eval-Print Loop) written in Rust. It provides a unified interface for executing code across 25 programming languages without the hassle of managing multiple compilers, interpreters, or build tools.

Whether you're a beginner learning your first programming language or an experienced polyglot developer, run streamlines your workflow by providing consistent commands and behavior across all supported languages.

## Who is this for?

• Beginners: Learn programming without worrying about complex setup procedures. Just install, run, and start coding in any language.

• Students: Quickly test code snippets and experiment with different programming paradigms across multiple languages.

• Developers: Prototype ideas rapidly, test algorithms, and switch between languages seamlessly without context switching.

• DevOps Engineers: Write and test automation scripts in various languages from a single tool.

• Educators: Teach programming concepts across multiple languages with a consistent interface.

## Why was the run created?

Traditional development workflows require installing and configuring separate tools for each programming language. This creates several problems:

• Time-consuming setup: Installing compilers, interpreters, package managers, and configuring environments for each language.

• Inconsistent interfaces: Each language has different commands and flags for compilation and execution.

• Cognitive overhead: Remembering different commands and workflows for each language.

• Barrier to entry: Beginners struggle with the setup before writing their first line of code.

Run solves these problems by providing a single, unified interface that handles all the complexity behind the scenes. You focus on writing code, and run takes care of the rest.

## Why Rust?

Run is built with Rust for several compelling reasons:

• Performance: Rust's zero-cost abstractions and efficient memory management ensure run starts instantly and executes with minimal overhead.

• Reliability: Rust's strong type system and ownership model prevent common bugs like null pointer dereferences and data races, making the run stable and crash-resistant.

• Cross-platform: Rust compiles to native code for Windows, macOS, and Linux, providing consistent behavior across all platforms.

• Memory safety: No garbage collector means predictable performance without unexpected pauses.

• Modern tooling: Cargo (Rust's package manager) makes building and distributing run straightforward.

• Future-proof: Rust's growing ecosystem and industry adoption ensure long-term maintainability.

---

## Quickstart

```bash
# Show build metadata for the current binary
run --version

# Execute a snippet explicitly
run --lang python --code "print('hello, polyglot world!')"

# Let run detect language from the file extension
run examples/go/hello/main.go

# Drop into the interactive REPL (type :help inside)
run

# Pipe stdin (here: JSON) into Node.js
echo '{"name":"Ada"}' | run js --code "const data = JSON.parse(require('fs').readFileSync(0, 'utf8')); console.log(`hi ${data.name}`)"

# Pipe stdin into Python
echo "Hello from stdin" | run python --code "import sys; print(sys.stdin.read().strip().upper())"

# Pipe stdin into Go
echo "world" | run go --code 'import "fmt"; import "bufio"; import "os"; scanner := bufio.NewScanner(os.Stdin); scanner.Scan(); fmt.Printf("Hello, %s!\n", scanner.Text())'
```

---

## Installation

All release assets are published on the [GitHub Releases](https://github.com/Esubaalew/run/releases) page, including macOS builds for both Apple Silicon (arm64) and Intel (x86\_64). Pick the method that fits your platform:

Installing the run is straightforward. Choose the method that works best for your system:

<details>
<summary><strong>Cargo (Rust)</strong></summary>
<pre><code class="language-bash">cargo install run-kit</code></pre>
<blockquote>
<p>Installs the <code>run</code> binary from the <a href="https://crates.io/crates/run-kit"><code>run-kit</code></a> crate. Updating? Run <code>cargo install run-kit --force</code>.</p>
</blockquote>
<pre><code class="language-bash"># Or build from source
git clone https://github.com/Esubaalew/run.git
cd run
cargo install --path .</code></pre>
<blockquote>
<p>This builds the run binary using your active Rust toolchain. The project targets Rust 1.70 or newer.</p>
</blockquote>
</details>

<details>
<summary><strong>Homebrew (macOS)</strong></summary>
<pre><code class="language-bash">brew install --formula https://github.com/Esubaalew/run/releases/latest/download/homebrew-run.rb</code></pre>
<blockquote>
<p>This formula is published as a standalone file on each release; it isn’t part of the default Homebrew taps. Installing by name (<code>brew install homebrew-run</code>) will fail—always point Homebrew to the release URL above (or download the file and run <code>brew install ./homebrew-run.rb</code>).</p>
</blockquote>
<p>Once the latest release artifacts are published, Homebrew automatically selects the correct macOS binary for your CPU (Intel or Apple Silicon) based on this formula.</p>
</details>

<details>
<summary><strong>Debian / Ubuntu</strong></summary>
<pre><code class="language-bash">curl -LO https://github.com/Esubaalew/run/releases/latest/download/run-deb.sha256
DEB_FILE=$(awk 
<details>
<summary><strong>Windows (Scoop)</strong></summary>
<pre><code class="language-powershell">scoop install https://github.com/Esubaalew/run/releases/latest/download/run-scoop.json</code></pre>
</details>
<details>
<summary><strong>Install script (macOS / Linux)</strong></summary>
<pre><code class="language-bash">curl -fsSLO https://raw.githubusercontent.com/Esubaalew/run/master/scripts/install.sh
chmod +x install.sh
./install.sh --add-path           # optional: append ~/.local/bin to PATH</code></pre>
<p>Pass <code>--version v0.2.0</code>, <code>--prefix /usr/local/bin</code>, or <code>--repo yourname/run</code> to customize the install.</p>
</details>
<details>
<summary><strong>Download the archive directly</strong></summary>
<ol>
<li>Grab the <code>tar.gz</code> (macOS/Linux) or <code>zip</code> (Windows) from the latest release.</li>
<li>Extract it and copy <code>run</code> / <code>run.exe</code> onto your <code>PATH</code>.</li>
<li>Optionally execute the bundled <code>install.sh</code> to handle the copy for you.</li>
</ol>
</details>
<details>
<summary><strong>Build from source</strong></summary>
<pre><code class="language-bash">cargo install run-kit</code></pre>
<p>The project targets Rust 1.70+. Installing from crates.io gives you the same <code>run</code> binary that CI publishes; use <code>--force</code> when upgrading to a newer release.</p>
</details>
<p>Verify installation:</p>
<pre><code class="language-bash"># Verify installation
run --version</code></pre>
<p>Output:</p>
<pre><code class="language-plaintext">run 0.1.1</code></pre>
<hr />
<h2>How it works</h2>
<p><code>run</code> shells out to real toolchains under the hood. Each <code>LanguageEngine</code> implements a small trait that knows how to:</p>
<ol>
<li>
<p>Detect whether the toolchain is available (e.g. <code>python3</code>, <code>go</code>, <code>rustc</code>).</p>
</li>
<li>
<p>Prepare a temporary workspace (compilation for compiled languages, transient scripts for interpreters).</p>
</li>
<li>
<p>Execute snippets, files, or stdin streams and surface stdout/stderr consistently.</p>
</li>
<li>
<p>Manage session state for the interactive REPL (persistent modules, stateful scripts, or regenerated translation units).</p>
</li>
</ol>
<p>This architecture keeps the core lightweight while making it easy to add new runtimes or swap implementations.</p>
<hr />
<h2>Supported languages</h2>
<p><code>run</code> supports 25+ languages:</p>
<p>Run supports 25 programming languages out of the box, covering a wide range of paradigms and use cases:</p>
<pre><code class="language-plaintext"># Scripting Languages
Python, JavaScript, Ruby, Bash, Lua, Perl, PHP

# Compiled Languages
Rust, Go, C, C++, Java, C#, Swift, Kotlin, Crystal, Zig, Nim

# Typed & Functional Languages
TypeScript, Haskell, Elixir, Julia

# Specialized Languages
R (Statistical computing)
Dart (Mobile development)</code></pre>
<table>
<thead>
<tr>
<th>Category</th>
<th>Languages & aliases</th>
<th>Toolchain expectations</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scripting & shells</strong></td>
<td>Bash (<code>bash</code>), Python (<code>py</code>, <code>python</code>), Ruby (<code>rb</code>, <code>ruby</code>), PHP (<code>php</code>), Perl (<code>perl</code>), Lua (<code>lua</code>), R (<code>r</code>), Elixir (<code>ex</code>, <code>elixir</code>)</td>
<td>Matching interpreter on <code>PATH</code></td>
</tr>
<tr>
<td><strong>Web & typed scripting</strong></td>
<td>JavaScript (<code>js</code>, <code>node</code>), TypeScript (<code>ts</code>, <code>deno</code>), Dart (<code>dart</code>), Kotlin (<code>kt</code>, <code>kotlin</code>)</td>
<td><code>node</code>, <code>deno</code>, <code>dart</code>, <code>kotlinc</code> + JRE</td>
</tr>
<tr>
<td><strong>Systems & compiled</strong></td>
<td>C (<code>c</code>), C++ (<code>cpp</code>, <code>cxx</code>), Rust (<code>rs</code>, <code>rust</code>), Go (<code>go</code>), Swift (<code>swift</code>), Zig (<code>zig</code>), Nim (<code>nim</code>), Haskell (<code>hs</code>, <code>haskell</code>), Crystal (<code>cr</code>, <code>crystal</code>), C# (<code>cs</code>, <code>csharp</code>), Java (<code>java</code>), Julia (<code>jl</code>, <code>julia</code>)</td>
<td>Respective compiler/toolchain</td>
</tr>
</tbody>
</table>
<h3>Categorization notes</h3>
<p>The categories above are usage-based to match how you’ll likely run code <code>run</code> rather than strict language taxonomies. Examples:</p>
<ul>
<li>
<p>Kotlin can target the JVM, Native, or JavaScript. If you’re using Kotlin/JS, it behaves more closely to the “Web & typed scripting” workflow, while Kotlin/JVM fits the “Systems & compiled” (with a JRE) approach.</p>
</li>
<li>
<p>Swift is listed under “Systems & compiled” because <code>swiftc</code> produces native binaries; however, you can still use it interactively via <code>run</code> for scripting-like workflows.</p>
</li>
<li>
<p>TypeScript typically runs at runtime via Node or Deno (after being transpiled), which is why it appears under “Web & typed scripting.”</p>
</li>
</ul>
<p>These groupings optimize for how commands are invoked and which toolchains <code>run</code> detects and orchestrates.</p>
<h3>Complete Language Aliases Reference</h3>
<p>Every language in run has multiple aliases for convenience. Use whichever feels most natural to you:</p>
<table>
<thead>
<tr>
<th>Alias</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>python, py, py3, python3</code></td>
<td>Python programming language</td>
</tr>
<tr>
<td><code>javascript, js, node, nodejs</code></td>
<td>JavaScript (Node.js runtime)</td>
</tr>
<tr>
<td><code>typescript, ts, ts-node, deno</code></td>
<td>TypeScript with type checking</td>
</tr>
<tr>
<td><code>rust, rs</code></td>
<td>Rust systems programming language</td>
</tr>
<tr>
<td><code>go, golang</code></td>
<td>Go programming language</td>
</tr>
<tr>
<td><code>c, gcc, clang</code></td>
<td>C programming language</td>
</tr>
<tr>
<td><code>cpp, c++, g++</code></td>
<td>C++ programming language</td>
</tr>
<tr>
<td><code>java</code></td>
<td>Java programming language</td>
</tr>
<tr>
<td><code>csharp, cs, dotnet</code></td>
<td>C# (.NET)</td>
</tr>
<tr>
<td><code>ruby, rb, irb</code></td>
<td>Ruby programming language</td>
</tr>
<tr>
<td><code>bash, sh, shell, zsh</code></td>
<td>Bash shell scripting</td>
</tr>
<tr>
<td><code>lua, luajit</code></td>
<td>Lua scripting language</td>
</tr>
<tr>
<td><code>perl, pl</code></td>
<td>Perl programming language</td>
</tr>
<tr>
<td><code>php, php-cli</code></td>
<td>PHP scripting language</td>
</tr>
<tr>
<td><code>haskell, hs, ghci</code></td>
<td>Haskell functional language</td>
</tr>
<tr>
<td><code>elixir, ex, exs, iex</code></td>
<td>Elixir functional language</td>
</tr>
<tr>
<td><code>julia, jl</code></td>
<td>Julia