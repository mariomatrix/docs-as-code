---
title: "Antigravity + Graphify: Free Tool Makes Google Antigravity 10x Smarter & Token-Efficient"
source: "https://www.youtube.com/watch?v=YwGUT6z0lQI&t=184s"
author:
  - "[[AI Stack Engineer]]"
published: 2026-04-28
created: 2026-05-03
description: "Graphify turns your codebase into a knowledge graph so every agent you spawn in Google Antigravity already understands your project. In this video I walk thr..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=YwGUT6z0lQI)

## Transcript

**0:00** · If you use Google Anti-gravity, you've probably watched this happen. You give the agent a task and before it writes a single line of code, it starts reading your readme, your config, your source files, one by one. It's trying to figure out what your project even is. Andre Karpathy talked about this problem publicly. He's one of the co-founders of OpenAI, used to lead AI at Tesla, and a lot of developers follow him for his takes on AI tooling. He keeps a folder on his machine where he dumps papers, tweets, screenshots, and notes.

**0:31** · And the issue he described is exactly what every anti-gravity user runs into. A pile of raw files and LLM has to scan from scratch every single time. And every one of those reads costs tokens, a lot of tokens. The agent burns through your context window just to understand the project and only then starts the actual work. Tomorrow you spawn a new agent for a new task and it starts the same loop all over again. No memory, no map, just raw file reads.

**1:01** · That's the wasted spend nobody talks about. There's a tool called Graphify that fixes this. It reads your project once, builds a knowledge graph of how everything connects, and every anti-gravity agent reads that graph at the start of any task instead of stumbling through your files blind. According to their own benchmark, Graphify reduces tokens per query by up to 71 and a half times compared to letting the agent read raw files.

**1:28** · Real world numbers will be smaller than that, but the savings on bigger projects are still huge, and the agents answers come out much more accurate. Let me show you how to set it up in anti-gravity. The way to think about it is simple. A regular anti-gravity agent is a freelancer you just hired. They know how to code, but they don't know your project. Graphify is the senior engineer who hands them the wiring diagram before they start.

**1:53** · They already know where the O lives, which services call which, where the rendering logic sits, and which five modules are the heart of the system. You build that diagram once, and every agent you spawn after that gets it for free.

**2:07** · And it's not only for code. You can point it at research papers, design docs, PDFs, meeting recordings, screenshots, even YouTube links. It handles all of that in a single graph.

**2:18** · But for this video, I'll stick to a code project so the steps stay clear. Under the hood, Graphify runs in three passes, and it's worth knowing what each one does because that's where the cost decisions live. The first pass parses your code with Treesitter. It supports around 23 languages: Python, JavaScript, TypeScript, Go, Rust, Java, C, C++, Ruby, Swift, Cotlin, and a bunch of others. This pass is fully local.

**2:43** · It reads every class, every function, every import, every call, and it costs you zero tokens because no model is called.

**2:53** · The second pass handles audio and video.

**2:56** · If you have meeting recordings, tutorials, or YouTube links in your folder, it transcribes them locally using faster whisper. Again, no API tokens. Nothing leaves your machine. The third pass is the only one that actually cost money. for markdown files, PDFs, images, readmes, and docs. It sends them through your model provider with parallel sub aents to extract concepts and relationships. This runs once per project. After that, the result is cached using a SHA 256 hash.

**3:25** · So when you change a file later and run an update, only that file gets reprocessed. You don't pay for the same content twice.

**3:35** · Everything merges into one graph. Then a clustering algorithm called leaden groups related nodes into communities.

**3:41** · No vector database, no embeddings. It's pure graph structure. Each community ends up being a kind of neighborhood like authentication logic or rendering or whatever your project is built around. All right, let's get to the install. Before anything, check your Python version. Graphy needs Python 3.10 or newer. If you're on something older, update it first because the install will fail or you'll hit weird errors later.

**4:06** · On Mac, just use Brew. On Windows, grab the latest installer from the Python website. On Linux, use your package manager. Once Python is sorted, open anti-gravity. Open the project folder you want to graph and open the built-in terminal. The install is two commands.

**4:23** · First one is pip install graphifyu. Pay attention to the spelling. The package name ends in double Y. There are other packages on Pippi with similar names that are not the official one, so don't grab the wrong one. After the package installs, run graphify install- d-platform antigravity. This copies the skill file into the right place for antigravity to pick it up. Next is the part that makes graphify always on. Run graphify antigravity install.

**4:52** · Antiggravity does not have tool hooks like some other agents do. So the way Graphify makes itself always available is by writing two files for you. It writes aagent/ruules/graphify.md which anti-gravity reads with every conversation and it writes aagent/workflows/graphify.md which registers /graphify as a slashcomand in the editor.

**5:16** · So now any agent you spawn in the agent manager already knows the graph exists and is told to read the graph report before doing anything else. This is the piece that actually changes the agents behavior day-to-day. Without it, you'd have to remind every new task to use the graph. With it installed, every agent in mission control just has the context automatically. Now let's build the graph. In the anti-gravity editor or terminal, type /graphify followed by a dot.

**5:46** · The dot just means current directory. You can also point it at a specific subfolder like /graphify/src if you want to graph just one part of your project. If your repo has stuff you want to skip, drop agraphify ignore file at the root. Same syntax asit ignore.

**6:06** · Put node modules vendor distext build folders whatever you don't want included. The first run takes a while.

**6:14** · For a medium project with a few hundred files mixed with some docs, expect somewhere around 10 to 15 minutes.

**6:21** · Progress shows as it goes. When it finishes, you get a folder called graphify- out with four things inside. A graph.html file you open in your browser, a graph report. MD, which is the highle summary, a graph.json, which is the full machine readable graph, and a cache folder. If you open graph.html, HTML, you'll see a star map of your project. Colored dots with lines between them. Each dot is a function, a class, a doc, a concept, an image, whatever was in your folder.

**6:51** · The big dots are what Graphify calls god nodes, the things everything else connects to. If 40 files in your codebase touch a specific module, that module shows up as a big node. Click any node and the side panel shows you which files it lives in. You can also filter by community. So if you want to look only at the O stuff, just uncheck the rest. Graphifies readme quotes a number 71 and a half times fewer tokens per query.

**7:17** · That's from a benchmark on a 52 file mixed corpus comparing loading every file into context versus reading the graph plus a few targeted sections. That's an extreme case. In normal anti-gravity usage, where the agent is already smart about what it reads, the savings are smaller, but the answer quality is much better.

**7:39** · Expect maybe 5 to 15% token reduction on smaller projects and a lot more on bigger ones with mixed content. The bigger your repo, the more you get out of it. Keeping the graph fresh matters, too. If you build it once and never update it, the agent will start using outdated info. Two options here.

**7:55** · Run graphify update by hand whenever you want and it only reprocesses files that actually changed. or run graphify hook install which wires up git hooks so the graph rebuilds on every commit and branch switch the git hook is the one

**8:14** · I'd use because you'll forget otherwise one thing worth being honest about if your project has under 10 files don't bother can handle that without help where graphify earns its place is on bigger projects with mixed content a real codebase with a docs folder a research project a folder of PDFs and meeting notes That's where the savings and the better agent answers compound. You can also query the graph from the terminal without spawning an agent.

**8:40** · Commands like graphify query followed by a question in quotes traverse the graph and give you an answer with file references. Graphy path finds the shortest connection between two concepts. Graphy explain gives you a plain language summary of any node. Useful for when you just want a quick answer. All right, so that's it from the video and I hope you enjoyed it.