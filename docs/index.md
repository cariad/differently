# differently

## Introduction

`differently` is a CLI tool and Python package for visualising the differences between things.

For example:

```bash
differently examples/1.md examples/2.md
```

<style type="text/css">.rst-content pre .thtml-code { background: black; }</style>

<!--dinject as=html host=terminal range=start-->

<style type="text/css">.thtml { --green: #0C0; --yellow: #CC0; --red: #C00; } .foreground-green { border-color: var(--green); color: var(--green); } .foreground-yellow { border-color: var(--yellow); color: var(--yellow); } .foreground-red { border-color: var(--red); color: var(--red); }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="foreground-green"># "differently" example file</span>                           <span class="foreground-green">=</span>  <span class="foreground-green"># "differently" example file</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-green">To run this example, install `differently` then run:</span>   <span class="foreground-green">=</span>  <span class="foreground-green">To run this example, install `differently` then run:</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-green">```bash</span>                                                <span class="foreground-green">=</span>  <span class="foreground-green">```bash</span><br /><span class="foreground-green">differently 1.md 2.md</span>                                  <span class="foreground-green">=</span>  <span class="foreground-green">differently 1.md 2.md</span><br /><span class="foreground-green">```</span>                                                    <span class="foreground-green">=</span>  <span class="foreground-green">```</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-yellow">This line says "foo" in 1.md.</span>                          <span class="foreground-yellow">~</span>  <span class="foreground-yellow">This line says "bar" in 2.md.</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-green">Now, a deletion:</span>                                       <span class="foreground-green">=</span>  <span class="foreground-green">Now, a deletion:</span><br />                                                       <span class="foreground-red">x</span><br /><span class="foreground-red">Hello from 1.md.</span>                                       <span class="foreground-red">x</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-green">The line above should appear in 1.md but deleted in</span>    <span class="foreground-green">=</span>  <span class="foreground-green">The line above should appear in 1.md but deleted in</span><br /><span class="foreground-green">the diff because it's not in 2.md.</span>                     <span class="foreground-green">=</span>  <span class="foreground-green">the diff because it's not in 2.md.</span><br />                                                       <span class="foreground-green">=</span><br /><span class="foreground-green">And finally, this next line doesn't exist in 1.md but</span>  <span class="foreground-green">=</span>  <span class="foreground-green">And finally, this next line doesn't exist in 1.md but</span><br /><span class="foreground-green">should be added in the diff because it's in 2.md:</span>      <span class="foreground-green">=</span>  <span class="foreground-green">should be added in the diff because it's in 2.md:</span><br />                                                       <span class="foreground-yellow">&gt;</span><br />                                                       <span class="foreground-yellow">&gt;</span>  <span class="foreground-yellow">Hello from 2.md.</span><br /></code></pre>

<!--dinject range=end-->

## Installation

`differently` requires **Python 3.8 or later**.

```bash
pip install differently
```

## Feedback

Please raise bugs, request features and ask questions at [github.com/cariad/differently/issues](https://github.com/cariad/differently/issues).

Mention if you're a [sponsor](https://github.com/sponsors/cariad) to ensure I respond as a priority. Thank you!

## Project

The source for `differently` is available at [github.com/cariad/differently](https://github.com/cariad/differently) under the MIT licence.

And, **hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).
