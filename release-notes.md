:robot: I have created a release *beep* *boop*
---


<details><summary>python-openinference-semantic-conventions: 0.1.22</summary>

## [0.1.22](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-semantic-conventions-v0.1.21...python-openinference-semantic-conventions-v0.1.22) (2025-09-18)


### Features

* Add semantic conventions for agent and graph attributes ([#1748](https://github.com/luke-moehlenbrock/openinference/issues/1748)) ([5f90a80](https://github.com/luke-moehlenbrock/openinference/commit/5f90a8014c216a821c299d0c7ea7aa79a4fc738d))
* **semantic-conventions:** enhance provider enum to include XAI and DeepSeek ([#1766](https://github.com/luke-moehlenbrock/openinference/issues/1766)) ([f7e125e](https://github.com/luke-moehlenbrock/openinference/commit/f7e125ea70c181b2a3f069bcca4bae3bb75a7d45))
* **semcov:** add audio token counts to semantic convention  ([#1453](https://github.com/luke-moehlenbrock/openinference/issues/1453)) ([ae5cd15](https://github.com/luke-moehlenbrock/openinference/commit/ae5cd15d0a702f976908d84a6d87847859c4685a))
* **semcov:** Cost semantic convention changes ([#1694](https://github.com/luke-moehlenbrock/openinference/issues/1694)) ([5f904bf](https://github.com/luke-moehlenbrock/openinference/commit/5f904bfad33e109843924aab1a609845a050d6f3))
* **semcov:** token counts for cached prompts and reasoning steps in the completion ([#1393](https://github.com/luke-moehlenbrock/openinference/issues/1393)) ([c4e2252](https://github.com/luke-moehlenbrock/openinference/commit/c4e225244adc287b9b011972bc980550939e126a))
* **semcov:** Update input and output cost ([#1774](https://github.com/luke-moehlenbrock/openinference/issues/1774)) ([c2ee804](https://github.com/luke-moehlenbrock/openinference/commit/c2ee804e63cb4b5ff393238854c37d99c6f5d675))


### Bug Fixes

* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation: 0.1.39</summary>

## [0.1.39](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-v0.1.38...python-openinference-instrumentation-v0.1.39) (2025-09-18)


### Features

* add context manager for capturing openinference spans ([#1781](https://github.com/luke-moehlenbrock/openinference/issues/1781)) ([aab3386](https://github.com/luke-moehlenbrock/openinference/commit/aab33868276627705f3e83fe8898429b71a23695))
* add instrumentation for google-adk ([#1759](https://github.com/luke-moehlenbrock/openinference/issues/1759)) ([aeb1769](https://github.com/luke-moehlenbrock/openinference/commit/aeb17692d30cd8112bcad0990f1ec56491a59962))
* add manual instrumentation helpers for llm spans ([#1424](https://github.com/luke-moehlenbrock/openinference/issues/1424)) ([ee79fa3](https://github.com/luke-moehlenbrock/openinference/commit/ee79fa35c247608f21b902b84443427ddf643314))
* Agno instrumentor ([#1603](https://github.com/luke-moehlenbrock/openinference/issues/1603)) ([50f30e2](https://github.com/luke-moehlenbrock/openinference/commit/50f30e26b5fcc074cc8a7dbbc34e9c11b7af0e41))
* Allow to hide llm.prompts span from trace config ([#1863](https://github.com/luke-moehlenbrock/openinference/issues/1863)) ([7d633d8](https://github.com/luke-moehlenbrock/openinference/commit/7d633d8fcf6ab5dbd8596a5900f3982db8e88d89))
* increase default span attribute count limit to 10,000 ([#2042](https://github.com/luke-moehlenbrock/openinference/issues/2042)) ([0e90576](https://github.com/luke-moehlenbrock/openinference/commit/0e90576cd841c73f561ffbb98d9a39cfe035509d))
* **instrumentation:** add dangerously_using_project context manager ([#2134](https://github.com/luke-moehlenbrock/openinference/issues/2134)) ([aed9db0](https://github.com/luke-moehlenbrock/openinference/commit/aed9db05b93d1ae0cb7d8a49977de1926b038740))
* **instrumentation:** add helpers for remaining semantic conventions ([#1606](https://github.com/luke-moehlenbrock/openinference/issues/1606)) ([cb3d4fa](https://github.com/luke-moehlenbrock/openinference/commit/cb3d4fa5f0b5d3281c60fa02fa9219813218e815))
* openai-agents instrumentation ([#1350](https://github.com/luke-moehlenbrock/openinference/issues/1350)) ([9afbad3](https://github.com/luke-moehlenbrock/openinference/commit/9afbad3100d68601a2f9265fe20985a34f80e04b))
* pydanticai instrumentation ([#1639](https://github.com/luke-moehlenbrock/openinference/issues/1639)) ([d8c5b9c](https://github.com/luke-moehlenbrock/openinference/commit/d8c5b9cdf793dcce247b2ea852c28eba3a1989bc))
* **python:** get_first_span_id via a context manager ([#2013](https://github.com/luke-moehlenbrock/openinference/issues/2013)) ([b0b080c](https://github.com/luke-moehlenbrock/openinference/commit/b0b080c564a2fb72b8f6796cad603f0166bcc767))


### Bug Fixes

* add type stubs for openinference span ([#1415](https://github.com/luke-moehlenbrock/openinference/issues/1415)) ([2170977](https://github.com/luke-moehlenbrock/openinference/commit/21709778f59c2fd31b1c14ee1bfb465e48771d5b))
* allow user override of id generator ([#1315](https://github.com/luke-moehlenbrock/openinference/issues/1315)) ([1916749](https://github.com/luke-moehlenbrock/openinference/commit/19167498fd74f2e93481bd63b5636e264af1eaab))
* Enable sampling when using OpenInference tracer ([#1782](https://github.com/luke-moehlenbrock/openinference/issues/1782)) ([b4007cf](https://github.com/luke-moehlenbrock/openinference/commit/b4007cffc5857028d6004aebd369877cab96d801))
* ensure `OpenInferenceSpan` is an instance of `opentelemetry.trace.Span` for type checks ([#1441](https://github.com/luke-moehlenbrock/openinference/issues/1441)) ([b2c8959](https://github.com/luke-moehlenbrock/openinference/commit/b2c895967e881444ff339d28b440375f6edaec74))
* ensure io attributes output by manual instrumentation helpers are always strings ([#1502](https://github.com/luke-moehlenbrock/openinference/issues/1502)) ([43c7f4a](https://github.com/luke-moehlenbrock/openinference/commit/43c7f4a41d9d36828d0f45907e7a580ce97dd68e))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
* update readmes for development setup and fixes ([#1629](https://github.com/luke-moehlenbrock/openinference/issues/1629)) ([7b211b3](https://github.com/luke-moehlenbrock/openinference/commit/7b211b3b1624ab433ba35568112f0a1d8964456f))
</details>

<details><summary>python-openinference-instrumentation-agno: 0.1.16</summary>

## [0.1.16](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-agno-v0.1.15...python-openinference-instrumentation-agno-v0.1.16) (2025-09-18)


### Features

* Agno instrumentor ([#1603](https://github.com/luke-moehlenbrock/openinference/issues/1603)) ([50f30e2](https://github.com/luke-moehlenbrock/openinference/commit/50f30e26b5fcc074cc8a7dbbc34e9c11b7af0e41))
* **Agno:** Capture agent graph attributes  ([#2090](https://github.com/luke-moehlenbrock/openinference/issues/2090)) ([7930348](https://github.com/luke-moehlenbrock/openinference/commit/7930348788c292958b3701119dc4c2837a341c53))
* **Agno:** Capture graph attributes for agent visual ([#2053](https://github.com/luke-moehlenbrock/openinference/issues/2053)) ([8d5ae09](https://github.com/luke-moehlenbrock/openinference/commit/8d5ae09b09fbcfaae7bab0dea25db3a2ad076a4d))
* **agno:** enable user tracking ([#1997](https://github.com/luke-moehlenbrock/openinference/issues/1997)) ([d76f5f1](https://github.com/luke-moehlenbrock/openinference/commit/d76f5f1ef112658a8286d9becf8c9f114b7bc911))
* enhance function call span attributes with input value and erro& ([#1836](https://github.com/luke-moehlenbrock/openinference/issues/1836)) ([5d239df](https://github.com/luke-moehlenbrock/openinference/commit/5d239dfbebcfaf34f276e9169be644b91eeafd09))
* Prioritize subclasses method wrapping to prevent multiple spans ([#1809](https://github.com/luke-moehlenbrock/openinference/issues/1809)) ([cc37471](https://github.com/luke-moehlenbrock/openinference/commit/cc37471bcf2be18ff205ab4e49654be42c27daee))
* Updates for new Agno verison ([#1647](https://github.com/luke-moehlenbrock/openinference/issues/1647)) ([8292d0d](https://github.com/luke-moehlenbrock/openinference/commit/8292d0d5620a9c58c4646e553704a31fd3f8cba3))


### Bug Fixes

* Agno duplicate model invoke ([#1614](https://github.com/luke-moehlenbrock/openinference/issues/1614)) ([919e776](https://github.com/luke-moehlenbrock/openinference/commit/919e776c41fc902f76e8da495c7618ae0ad84292))
* Agno v2 fixes ([#2211](https://github.com/luke-moehlenbrock/openinference/issues/2211)) ([278f570](https://github.com/luke-moehlenbrock/openinference/commit/278f570130635d99672126554b9d3a950c658ff4))
* **agno:** Allow agent.name to be `None` in `arun`. ([#1621](https://github.com/luke-moehlenbrock/openinference/issues/1621)) ([5288979](https://github.com/luke-moehlenbrock/openinference/commit/52889796daa5ac221af21b76d77b80e594cdcf89))
* **agno:** capture session_id and user_id for teams too ([#2086](https://github.com/luke-moehlenbrock/openinference/issues/2086)) ([0a51d50](https://github.com/luke-moehlenbrock/openinference/commit/0a51d50be89a440d6df2fca90fe72ab730ee7267))
* correct usage of user id & session id ([#2138](https://github.com/luke-moehlenbrock/openinference/issues/2138)) ([165b7e8](https://github.com/luke-moehlenbrock/openinference/commit/165b7e890cb9691ff1ab3890288c97dc046f1a1b))
* filter sensitive model params ([#1737](https://github.com/luke-moehlenbrock/openinference/issues/1737)) ([fe7ebbe](https://github.com/luke-moehlenbrock/openinference/commit/fe7ebbe9f7663e39d6f18ee1be9f775f0f6e7fb4))
* handle AgnoInstrumentor failing with OpenAIResponses ([#1701](https://github.com/luke-moehlenbrock/openinference/issues/1701)) ([f33fadf](https://github.com/luke-moehlenbrock/openinference/commit/f33fadf5a67fd4bce8ba590cdae4c9b7d1133d74))
* nullable agent.name in agno instrumentation arun ([#1803](https://github.com/luke-moehlenbrock/openinference/issues/1803)) ([c2cc388](https://github.com/luke-moehlenbrock/openinference/commit/c2cc3884c3eb2ba00ddb992cc7b2aff1709bd891))
</details>

<details><summary>python-openinference-instrumentation-mistralai: 1.4.0</summary>

## [1.4.0](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-mistralai-v1.3.3...python-openinference-instrumentation-mistralai-v1.4.0) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* remove mistralai dependency in mistralai instrumentor ([#1271](https://github.com/luke-moehlenbrock/openinference/issues/1271)) ([17c0ce5](https://github.com/luke-moehlenbrock/openinference/commit/17c0ce5a1ddc48a5c7a835f09941569232458f76))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-openai: 0.1.33</summary>

## [0.1.33](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-openai-v0.1.32...python-openinference-instrumentation-openai-v0.1.33) (2025-09-18)


### Features

* add cached read semantic conventions to openai sdk ([#1485](https://github.com/luke-moehlenbrock/openinference/issues/1485)) ([2db5918](https://github.com/luke-moehlenbrock/openinference/commit/2db591850259c1ff1fe606151f7f8be1ec1d63a7))
* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* instrument OpenAI responses API ([#1521](https://github.com/luke-moehlenbrock/openinference/issues/1521)) ([64cde2b](https://github.com/luke-moehlenbrock/openinference/commit/64cde2b7230bfae3e7f7fb1141708a86ceea6b1a))
* openai + openai agent support custom tool calls ([#2080](https://github.com/luke-moehlenbrock/openinference/issues/2080)) ([ee8693c](https://github.com/luke-moehlenbrock/openinference/commit/ee8693c3325380440e4af4e0df708851c5598c30))
* Openai audio + reasoning token counts ([#1547](https://github.com/luke-moehlenbrock/openinference/issues/1547)) ([cbae31b](https://github.com/luke-moehlenbrock/openinference/commit/cbae31b2838234a3fe388a1501caadd281ac545e))
* **openai:** implement image redaction for input values when hide_input_images=True ([#2146](https://github.com/luke-moehlenbrock/openinference/issues/2146)) ([fac0604](https://github.com/luke-moehlenbrock/openinference/commit/fac0604caeedf0b0332151dfde69f0b51b554652))


### Bug Fixes

* CI Failures For OpenAI & OpenAI Agents ([#1725](https://github.com/luke-moehlenbrock/openinference/issues/1725)) ([69576ca](https://github.com/luke-moehlenbrock/openinference/commit/69576cac4628f7d3b1b36558ad6cf8e4ae65b2d8))
* CI Failures For OpenAI & OpenAI Agents Follow Up ([#1733](https://github.com/luke-moehlenbrock/openinference/issues/1733)) ([ec1e855](https://github.com/luke-moehlenbrock/openinference/commit/ec1e8552b40c8a04ee2b3b92073e41e405b95293))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* ruff formating fix & bump ruff version in dev requirements ([#1600](https://github.com/luke-moehlenbrock/openinference/issues/1600)) ([076bb79](https://github.com/luke-moehlenbrock/openinference/commit/076bb7966d44fccdb2ab94e6f379ef4ae22c39b1))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-openai-agents: 2.0.0</summary>

## [2.0.0](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-openai-agents-v1.3.0...python-openinference-instrumentation-openai-agents-v2.0.0) (2025-09-18)


### � BREAKING CHANGES

* set openinference processor as the exclusive processor by default ([#1792](https://github.com/luke-moehlenbrock/openinference/issues/1792))

### Features

* cached and reasoning tokens from response api ([#1461](https://github.com/luke-moehlenbrock/openinference/issues/1461)) ([a9f257c](https://github.com/luke-moehlenbrock/openinference/commit/a9f257c1dee46eb18ed32f463bdc50cc7cab60fe))
* capture result from MCPListToolsSpanData ([#1458](https://github.com/luke-moehlenbrock/openinference/issues/1458)) ([66abe50](https://github.com/luke-moehlenbrock/openinference/commit/66abe50f187a45ce11fb64f3399b52a3139fe115))
* openai + openai agent support custom tool calls ([#2080](https://github.com/luke-moehlenbrock/openinference/issues/2080)) ([ee8693c](https://github.com/luke-moehlenbrock/openinference/commit/ee8693c3325380440e4af4e0df708851c5598c30))
* openai-agents instrumentation ([#1350](https://github.com/luke-moehlenbrock/openinference/issues/1350)) ([9afbad3](https://github.com/luke-moehlenbrock/openinference/commit/9afbad3100d68601a2f9265fe20985a34f80e04b))
* **openai-agents:** add support for exclusive processor configuration ([#1586](https://github.com/luke-moehlenbrock/openinference/issues/1586)) ([47c2ac3](https://github.com/luke-moehlenbrock/openinference/commit/47c2ac350a113bf7df45fbcebdfc19504e73723c))
* **openai-agents:** capture graph.node.id and graph.node.parent_id semantics  ([#1854](https://github.com/luke-moehlenbrock/openinference/issues/1854)) ([0864c13](https://github.com/luke-moehlenbrock/openinference/commit/0864c13fdfa9e289468ac0a79a2860a155be46de))
* **openai:** implement image redaction for input values when hide_input_images=True ([#2146](https://github.com/luke-moehlenbrock/openinference/issues/2146)) ([fac0604](https://github.com/luke-moehlenbrock/openinference/commit/fac0604caeedf0b0332151dfde69f0b51b554652))
* set openinference processor as the exclusive processor by default ([#1792](https://github.com/luke-moehlenbrock/openinference/issues/1792)) ([d56abb1](https://github.com/luke-moehlenbrock/openinference/commit/d56abb1935aa4a96925214c39cef045381ab9b15))


### Bug Fixes

* add span attributes for FunctionSpanData ([#1408](https://github.com/luke-moehlenbrock/openinference/issues/1408)) ([48d1a35](https://github.com/luke-moehlenbrock/openinference/commit/48d1a3549eb8dda55e941cab867d9581a96fdf33))
* attach span to otel context on span start ([#1373](https://github.com/luke-moehlenbrock/openinference/issues/1373)) ([b44809f](https://github.com/luke-moehlenbrock/openinference/commit/b44809f1c460dd3a9bee4a9b068e6c275fecf9b4))
* CI Failures For OpenAI & OpenAI Agents ([#1725](https://github.com/luke-moehlenbrock/openinference/issues/1725)) ([69576ca](https://github.com/luke-moehlenbrock/openinference/commit/69576cac4628f7d3b1b36558ad6cf8e4ae65b2d8))
* CI Failures For OpenAI & OpenAI Agents Follow Up ([#1733](https://github.com/luke-moehlenbrock/openinference/issues/1733)) ([ec1e855](https://github.com/luke-moehlenbrock/openinference/commit/ec1e8552b40c8a04ee2b3b92073e41e405b95293))
* classify handoff span as tool span ([#1374](https://github.com/luke-moehlenbrock/openinference/issues/1374)) ([e75a444](https://github.com/luke-moehlenbrock/openinference/commit/e75a444d766d900ec3bc78b9d257453fb0e586d1))
* fix IndexError for empty function output ([#1878](https://github.com/luke-moehlenbrock/openinference/issues/1878)) ([e6453e7](https://github.com/luke-moehlenbrock/openinference/commit/e6453e72784aac519e05c98b541a551500b814a4))
* get attributes from GenerationSpanData (i.e. chat completions api) ([#1426](https://github.com/luke-moehlenbrock/openinference/issues/1426)) ([c0f238d](https://github.com/luke-moehlenbrock/openinference/commit/c0f238d36f18bdec0062e84ca4e53a66c63508e0))
* handle error: invalid type dict in attribute 'output.value' value sequence ([#1443](https://github.com/luke-moehlenbrock/openinference/issues/1443)) ([34bacfd](https://github.com/luke-moehlenbrock/openinference/commit/34bacfd9369dfb098e931cf20982b286fcb7fbea))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* openai agent with int tool return ([#1419](https://github.com/luke-moehlenbrock/openinference/issues/1419)) ([1bb75a9](https://github.com/luke-moehlenbrock/openinference/commit/1bb75a94999bbe8615cdc7a5490fb2668833742f))
* **openai_agents:** Set status `on_span_end`. ([#1556](https://github.com/luke-moehlenbrock/openinference/issues/1556)) ([2b53efa](https://github.com/luke-moehlenbrock/openinference/commit/2b53efa491d81ab5852387f5a4d2e87972262616))
* openai-agents CI add eval_type_backport dependency for Python &lt;3.10 compatibility ([#2004](https://github.com/luke-moehlenbrock/openinference/issues/2004)) ([f38ed8e](https://github.com/luke-moehlenbrock/openinference/commit/f38ed8efe6734297a3e77c0b4d4ddde32bc8ba11))
* ruff formating fix & bump ruff version in dev requirements ([#1600](https://github.com/luke-moehlenbrock/openinference/issues/1600)) ([076bb79](https://github.com/luke-moehlenbrock/openinference/commit/076bb7966d44fccdb2ab94e6f379ef4ae22c39b1))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))
</details>

<details><summary>python-openinference-instrumentation-vertexai: 0.1.12</summary>

## [0.1.12](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-vertexai-v0.1.11...python-openinference-instrumentation-vertexai-v0.1.12) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* support function call parts when streaming ([#1587](https://github.com/luke-moehlenbrock/openinference/issues/1587)) ([43abca2](https://github.com/luke-moehlenbrock/openinference/commit/43abca26f75277f1a605389b1e99a19220104820))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-llama-index: 5.0.0</summary>

## [5.0.0](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-llama-index-v4.3.5...python-openinference-instrumentation-llama-index-v5.0.0) (2025-09-18)


### � BREAKING CHANGES

* support chat message content blocks for llama-index >= 0.12.3 ([#1446](https://github.com/luke-moehlenbrock/openinference/issues/1446))

### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* add toggle to separate trace from runtime context ([#1464](https://github.com/luke-moehlenbrock/openinference/issues/1464)) ([0865a69](https://github.com/luke-moehlenbrock/openinference/commit/0865a69904119676703e5ca26600458dd9fb60f2))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* **llama-index py:** capture reasoning, cache, and audio tokens ([#1489](https://github.com/luke-moehlenbrock/openinference/issues/1489)) ([9d0ec39](https://github.com/luke-moehlenbrock/openinference/commit/9d0ec3991a6adf7932b0b2069f38a6e83bb1b752))
* **llama-index:** Add LLM provider detection with lazy imports - res& ([#1710](https://github.com/luke-moehlenbrock/openinference/issues/1710)) ([f20ac82](https://github.com/luke-moehlenbrock/openinference/commit/f20ac827b1b38fe298e69753f6718b52e0807aa0))
* support chat message content blocks for llama-index &gt;= 0.12.3 ([#1446](https://github.com/luke-moehlenbrock/openinference/issues/1446)) ([291dc0a](https://github.com/luke-moehlenbrock/openinference/commit/291dc0a8d071f6b3a25b5b5cd8a5fe2d756a3cda))


### Bug Fixes

* Bump llama index version for tests + fix tests ([#1992](https://github.com/luke-moehlenbrock/openinference/issues/1992)) ([a70bcd5](https://github.com/luke-moehlenbrock/openinference/commit/a70bcd5090568dcf48b56cc2feb081d33febf3de))
* capture tools from chat kwargs ([#1509](https://github.com/luke-moehlenbrock/openinference/issues/1509)) ([2083836](https://github.com/luke-moehlenbrock/openinference/commit/2083836872dd9b3f4c40bcf66a2c3054f30aa59a))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* llama-index support vertex-ai token counts ([#1986](https://github.com/luke-moehlenbrock/openinference/issues/1986)) ([f75b573](https://github.com/luke-moehlenbrock/openinference/commit/f75b573fe09851a2708de8aa26fef388138256c3))
* **llama-index:** Capture tool call id from additional_kwargs ([#1299](https://github.com/luke-moehlenbrock/openinference/issues/1299)) ([14c1c0c](https://github.com/luke-moehlenbrock/openinference/commit/14c1c0c8f206a00f6cf67a9c1995c24283687f37))
* **llama-index:** fix typo in llama-index entry point ([#1288](https://github.com/luke-moehlenbrock/openinference/issues/1288)) ([15f3b59](https://github.com/luke-moehlenbrock/openinference/commit/15f3b5949121ce9c71f5f41d098858e492d4f5dd))
* **llama-index:** handle BaseAgent import changes in v0.13.0+ ([#2023](https://github.com/luke-moehlenbrock/openinference/issues/2023)) ([62ce073](https://github.com/luke-moehlenbrock/openinference/commit/62ce073c98887851dd02dfd785b791e7e7ca9cb5))
* **llama-index:** tools ui fix ([#1802](https://github.com/luke-moehlenbrock/openinference/issues/1802)) ([c81bda4](https://github.com/luke-moehlenbrock/openinference/commit/c81bda4e490677913e72d48509112f544970d57c))
* non-ascii characters in input.value ([#2199](https://github.com/luke-moehlenbrock/openinference/issues/2199)) ([8bfdd0d](https://github.com/luke-moehlenbrock/openinference/commit/8bfdd0d65aae74649a1087ec6796193485e0a73b))
* replace logger.exception() with repr() ([#1385](https://github.com/luke-moehlenbrock/openinference/issues/1385)) ([3b924da](https://github.com/luke-moehlenbrock/openinference/commit/3b924da0b823e23c9170a6dae682bb0488c884cb))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-dspy: 0.1.30</summary>

## [0.1.30](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-dspy-v0.1.29...python-openinference-instrumentation-dspy-v0.1.30) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* Add model name and provider fields to DSPy for better model tracking/instrumentation [#1730](https://github.com/luke-moehlenbrock/openinference/issues/1730) ([#1730](https://github.com/luke-moehlenbrock/openinference/issues/1730)) ([3613f66](https://github.com/luke-moehlenbrock/openinference/commit/3613f66331d3529f9131c2b9432696a79a4b7b21))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* **dspy:** Add initial support for async tracing ([#1597](https://github.com/luke-moehlenbrock/openinference/issues/1597)) ([205bdf0](https://github.com/luke-moehlenbrock/openinference/commit/205bdf0e3a8da1c86802735112d9eff9f8dd0c5f))
* **dspy:** Display Module.forward Output in JSON Format ([#1729](https://github.com/luke-moehlenbrock/openinference/issues/1729)) ([591a2d9](https://github.com/luke-moehlenbrock/openinference/commit/591a2d921d6fa09342059d71d43da46076ba8fad))
* **dspy:** Instrument DSPy DummyLM ([#2067](https://github.com/luke-moehlenbrock/openinference/issues/2067)) ([0b0349d](https://github.com/luke-moehlenbrock/openinference/commit/0b0349d14f227ac6b51fdf461c4e614e8b80582a))
* **dspy:** Instrument DSPy.Tool ([#1617](https://github.com/luke-moehlenbrock/openinference/issues/1617)) ([e1ee8ff](https://github.com/luke-moehlenbrock/openinference/commit/e1ee8ff86148a3fe0a8abf69bde675c8e0491cf5))


### Bug Fixes

* **dspy:** dspy 2.6.0 upgrade ([#1249](https://github.com/luke-moehlenbrock/openinference/issues/1249)) ([c1ab1d8](https://github.com/luke-moehlenbrock/openinference/commit/c1ab1d86783c607c2114c92245a17ed9754ff2f4))
* **dspy:** mask api keys passed as arguments ([#1990](https://github.com/luke-moehlenbrock/openinference/issues/1990)) ([98218a1](https://github.com/luke-moehlenbrock/openinference/commit/98218a1bf710f860a93eb941194e2abcc2eec63f))
* **dspy:** replace configure() with context() in async tests ([#2178](https://github.com/luke-moehlenbrock/openinference/issues/2178)) ([90c59e0](https://github.com/luke-moehlenbrock/openinference/commit/90c59e01c48a0d89a93172ed8e9d2436117b7cbc))
* **dspy:** upstream max token default value change ([#1718](https://github.com/luke-moehlenbrock/openinference/issues/1718)) ([1654bc1](https://github.com/luke-moehlenbrock/openinference/commit/1654bc1e0734b0424f67d678ad1e5e4271a9942c))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* **instrumentation-dspy:** pin urllib3&lt;2.0 for pytest-recording compatibility ([#2007](https://github.com/luke-moehlenbrock/openinference/issues/2007)) ([51f5040](https://github.com/luke-moehlenbrock/openinference/commit/51f5040af8bef8f7407dde7451ea1f2fb6ca7950))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-bedrock: 0.1.28</summary>

## [0.1.28](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-bedrock-v0.1.27...python-openinference-instrumentation-bedrock-v0.1.28) (2025-09-18)


### Features

* Add bedrock-agent instrumentation ([#1363](https://github.com/luke-moehlenbrock/openinference/issues/1363)) ([e174240](https://github.com/luke-moehlenbrock/openinference/commit/e174240a09db59c74b816efb3bc3176cc581d31e))
* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* **bedrock:** Add instrumentation for guardrailTrace ([#2058](https://github.com/luke-moehlenbrock/openinference/issues/2058)) ([8ea1eef](https://github.com/luke-moehlenbrock/openinference/commit/8ea1eef5db0a334c5ca66c77f7217246156d7ef0))
* **bedrock:** added support for retrieve, retrieve and generate ([#1786](https://github.com/luke-moehlenbrock/openinference/issues/1786)) ([2652fa7](https://github.com/luke-moehlenbrock/openinference/commit/2652fa7372a02980b55425591f16b61626db297c))
* **bedrock:** Multi Agent Support, capturing time metrics from metadata ([#1656](https://github.com/luke-moehlenbrock/openinference/issues/1656)) ([ed367a2](https://github.com/luke-moehlenbrock/openinference/commit/ed367a2707dd00d1e2fd9b7249deecd08ddd466f))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* Added exception to span when invoke_agent throws an exception  ([#1742](https://github.com/luke-moehlenbrock/openinference/issues/1742)) ([1027d18](https://github.com/luke-moehlenbrock/openinference/commit/1027d185ed233edacf8cfc76993c761a3b6a8afe))
* **bedrock:** fixing invoke model api calls ([#1760](https://github.com/luke-moehlenbrock/openinference/issues/1760)) ([0ce91a5](https://github.com/luke-moehlenbrock/openinference/commit/0ce91a5da29c36160b16da7194c4c59dca24bed4))
* **bedrock:** Included apipath into metadata ([#1775](https://github.com/luke-moehlenbrock/openinference/issues/1775)) ([081d630](https://github.com/luke-moehlenbrock/openinference/commit/081d630d2147134574cf2dd47630592d58e5f00d))
* image source types for anthropic 0.49 ([#1320](https://github.com/luke-moehlenbrock/openinference/issues/1320)) ([f022141](https://github.com/luke-moehlenbrock/openinference/commit/f022141b990bfd1de53b4c2e9c3f32d238d27048))
* include cache tokens in prompt tokens for anthropic ([#1429](https://github.com/luke-moehlenbrock/openinference/issues/1429)) ([abd36c4](https://github.com/luke-moehlenbrock/openinference/commit/abd36c45ea4ff966b58eccee42de252bc876d5ab))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* ruff formating fix & bump ruff version in dev requirements ([#1600](https://github.com/luke-moehlenbrock/openinference/issues/1600)) ([076bb79](https://github.com/luke-moehlenbrock/openinference/commit/076bb7966d44fccdb2ab94e6f379ef4ae22c39b1))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-langchain: 0.1.53</summary>

## [0.1.53](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-langchain-v0.1.52...python-openinference-instrumentation-langchain-v0.1.53) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* add span attributes `llm.provider` and `llm.system` to langchain instrumentation ([#1791](https://github.com/luke-moehlenbrock/openinference/issues/1791)) ([545f52d](https://github.com/luke-moehlenbrock/openinference/commit/545f52d25ce803410d92ba7f18da8bf2a8d87087))
* add toggle to separate trace from runtime context ([#1464](https://github.com/luke-moehlenbrock/openinference/issues/1464)) ([0865a69](https://github.com/luke-moehlenbrock/openinference/commit/0865a69904119676703e5ca26600458dd9fb60f2))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* Instrument sssistant tool calls made by LangGraph  ([#2012](https://github.com/luke-moehlenbrock/openinference/issues/2012)) ([f0e5852](https://github.com/luke-moehlenbrock/openinference/commit/f0e585258aca591dbb4e97cc1a7503b56971cebc))
* **langchainpy:** capture reasoning, cache, and audio tokens  ([#1480](https://github.com/luke-moehlenbrock/openinference/issues/1480)) ([22d962b](https://github.com/luke-moehlenbrock/openinference/commit/22d962b7c07b5293cde02209b6702b77cd8fc0f3))
* **langchain:** track tool schemas from LLM invocation parameters ([#1643](https://github.com/luke-moehlenbrock/openinference/issues/1643)) ([65d3a82](https://github.com/luke-moehlenbrock/openinference/commit/65d3a8219a1a061a4fdea19b17760096b5aca76a))
* unwrap input output keys from io values ([#1993](https://github.com/luke-moehlenbrock/openinference/issues/1993)) ([534c727](https://github.com/luke-moehlenbrock/openinference/commit/534c72764a72cfd995ecf3d0f70ecaafc7cf359a))


### Bug Fixes

* handle missing attribute if .instrument() has not been called and tracer has not been initialized ([#1340](https://github.com/luke-moehlenbrock/openinference/issues/1340)) ([2582513](https://github.com/luke-moehlenbrock/openinference/commit/2582513ef60dc510fc3f63930b9717edfe07b9a2))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* **langchain:** don't treat langgraph agent commands as exceptions ([#1389](https://github.com/luke-moehlenbrock/openinference/issues/1389)) ([af48af3](https://github.com/luke-moehlenbrock/openinference/commit/af48af39afb002d63e78d77b2d0ec543442410e1))
* **Langchain:** Handle custom data in additional kwargs ([#1898](https://github.com/luke-moehlenbrock/openinference/issues/1898)) ([c7f71e1](https://github.com/luke-moehlenbrock/openinference/commit/c7f71e19a128ff6054cd66120bb00b79d70e51ef))
* **Langchain:** map UsageMetadata object ([#2136](https://github.com/luke-moehlenbrock/openinference/issues/2136)) ([dab6cfd](https://github.com/luke-moehlenbrock/openinference/commit/dab6cfd72e6e537f0e8d0b5f78285f46182501fa))
* merge metadata ([#1497](https://github.com/luke-moehlenbrock/openinference/issues/1497)) ([793101a](https://github.com/luke-moehlenbrock/openinference/commit/793101a74570c0a4611c751ef518879486fdf852))
* message content when it's list of strings ([#1337](https://github.com/luke-moehlenbrock/openinference/issues/1337)) ([d79f90e](https://github.com/luke-moehlenbrock/openinference/commit/d79f90e8949da449bc0beef0f6ece75077d57e89))
* small typo in str() call ([#1822](https://github.com/luke-moehlenbrock/openinference/issues/1822)) ([4a7385b](https://github.com/luke-moehlenbrock/openinference/commit/4a7385b968330e420c67a9a9066fc0f95b4109c5))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* tool call for anthropic bedrock invoke model ([#1995](https://github.com/luke-moehlenbrock/openinference/issues/1995)) ([c26ffe5](https://github.com/luke-moehlenbrock/openinference/commit/c26ffe57e696221cd82c32e262b4cc8fd32fbe8a))
* tuple message type ([#1488](https://github.com/luke-moehlenbrock/openinference/issues/1488)) ([6b65b65](https://github.com/luke-moehlenbrock/openinference/commit/6b65b656627d7910a82a0c14c70c916b0b454a3b))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))
* use `llm_output` and `metadata` for model name ([#1819](https://github.com/luke-moehlenbrock/openinference/issues/1819)) ([8cb7439](https://github.com/luke-moehlenbrock/openinference/commit/8cb7439daf45910f918468651624519de1c1b8de))


### Documentation

* create gemini_tracing.py ([#1456](https://github.com/luke-moehlenbrock/openinference/issues/1456)) ([46e135f](https://github.com/luke-moehlenbrock/openinference/commit/46e135fdc394234e80510808fbd8b04746365b66))
* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-guardrails: 0.1.10</summary>

## [0.1.10](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-guardrails-v0.1.9...python-openinference-instrumentation-guardrails-v0.1.10) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-crewai: 0.1.14</summary>

## [0.1.14](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-crewai-v0.1.13...python-openinference-instrumentation-crewai-v0.1.14) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* **crewai:** capture graph.node.id and graph.node.parent_id semantics ([#1794](https://github.com/luke-moehlenbrock/openinference/issues/1794)) ([4645932](https://github.com/luke-moehlenbrock/openinference/commit/4645932b68f7ed5ab3ecd8818ddad9e1011c027e))
* **crewai:** enhance span naming to include crew, agent, and tool context ([#2202](https://github.com/luke-moehlenbrock/openinference/issues/2202)) ([af44991](https://github.com/luke-moehlenbrock/openinference/commit/af44991003f70fc21701b2f1ead8a19554cd37e2))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* **crewai:** crewai default empty tasks ([#1682](https://github.com/luke-moehlenbrock/openinference/issues/1682)) ([4a47bfc](https://github.com/luke-moehlenbrock/openinference/commit/4a47bfc065b88b55bfcb7605abf66ef12a286ec9))
* **crewai:** Not Getting Inputs For CrewAI Root Span ([#2193](https://github.com/luke-moehlenbrock/openinference/issues/2193)) ([9cf3b8f](https://github.com/luke-moehlenbrock/openinference/commit/9cf3b8fa0f432f6b6f783fc25a9d3d78f9164d4e))
* fix test failures with crew-latest ([#1282](https://github.com/luke-moehlenbrock/openinference/issues/1282)) ([e2e3dd1](https://github.com/luke-moehlenbrock/openinference/commit/e2e3dd13bf78a3ad4b0d44fc2ae2151127583dce))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-haystack: 0.1.25</summary>

## [0.1.25](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-haystack-v0.1.24...python-openinference-instrumentation-haystack-v0.1.25) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* CI Failures For Haystack ([#1736](https://github.com/luke-moehlenbrock/openinference/issues/1736)) ([673dc40](https://github.com/luke-moehlenbrock/openinference/commit/673dc4071845aa3282f9516de6a57d4c92790240))
* **haystack:** fixing ci issues for haystack-ai ([#1623](https://github.com/luke-moehlenbrock/openinference/issues/1623)) ([daffa8e](https://github.com/luke-moehlenbrock/openinference/commit/daffa8e3fa9825daa76268a91a208b8c77dd1cb1))
* **haystack:** update haystack for compatibility with 2.10 ([#1295](https://github.com/luke-moehlenbrock/openinference/issues/1295)) ([2f6c607](https://github.com/luke-moehlenbrock/openinference/commit/2f6c6078e4e1412306bbf954e2f9ad35336f3abc))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* ruff formating fix & bump ruff version in dev requirements ([#1600](https://github.com/luke-moehlenbrock/openinference/issues/1600)) ([076bb79](https://github.com/luke-moehlenbrock/openinference/commit/076bb7966d44fccdb2ab94e6f379ef4ae22c39b1))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-litellm: 0.1.26</summary>

## [0.1.26](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-litellm-v0.1.25...python-openinference-instrumentation-litellm-v0.1.26) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* **litellm:** add llm provider attributes ([#2094](https://github.com/luke-moehlenbrock/openinference/issues/2094)) ([86e681a](https://github.com/luke-moehlenbrock/openinference/commit/86e681aaf98116016848fc7d1b6c26a8c6607a25))
* **litellm:** track tool schemas from kwargs in litellm completion functions ([#1865](https://github.com/luke-moehlenbrock/openinference/issues/1865)) ([4df17c3](https://github.com/luke-moehlenbrock/openinference/commit/4df17c3562c1168db14af86fe5173b00e1ffadeb))
* reasoning, cache, audio token counts litellm ([#1516](https://github.com/luke-moehlenbrock/openinference/issues/1516)) ([89fd465](https://github.com/luke-moehlenbrock/openinference/commit/89fd465ff432d001fbca9cd3e4cca57bcf476d8a))


### Bug Fixes

* Add support for litellm Message type ([#1308](https://github.com/luke-moehlenbrock/openinference/issues/1308)) ([1f2407b](https://github.com/luke-moehlenbrock/openinference/commit/1f2407b2047fdf952109520fb010cd6ef6aa96ec))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* **litellm:** display tool_calls from model output ([#1722](https://github.com/luke-moehlenbrock/openinference/issues/1722)) ([53c9fa5](https://github.com/luke-moehlenbrock/openinference/commit/53c9fa5498135728364d122eefe2bf23ea30b47c))
* **litellm:** Fixing Invocation Params, Output Messages ([#1838](https://github.com/luke-moehlenbrock/openinference/issues/1838)) ([9f15912](https://github.com/luke-moehlenbrock/openinference/commit/9f15912bc87e697e1021db0b63e9d2c8b3d1e377))
* **litellm:** full JSON output ([#1735](https://github.com/luke-moehlenbrock/openinference/issues/1735)) ([891fc26](https://github.com/luke-moehlenbrock/openinference/commit/891fc265cd4a4c5600e7dd261e78ad4ad14e9cc6))
* **litellm:** remove sensitive info from invocation params ([#1571](https://github.com/luke-moehlenbrock/openinference/issues/1571)) ([fe4f784](https://github.com/luke-moehlenbrock/openinference/commit/fe4f784a020db96f41a2a1f49b1fe8a497369933))
* **liteLLM:** support sync stream ([#1307](https://github.com/luke-moehlenbrock/openinference/issues/1307)) ([5c04fa0](https://github.com/luke-moehlenbrock/openinference/commit/5c04fa0e10cd95db50e11b1be9afa0f2c3a39aa5))
* Missing Span Status In LiteLLM ([#1754](https://github.com/luke-moehlenbrock/openinference/issues/1754)) ([126f816](https://github.com/luke-moehlenbrock/openinference/commit/126f816577bf4450e0c15c3ac8fa8f7f754c58e5))
* Start span before API call ([#1562](https://github.com/luke-moehlenbrock/openinference/issues/1562)) ([7d9306b](https://github.com/luke-moehlenbrock/openinference/commit/7d9306b2f0654600b0a19c06319895470368fdde))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))
* use safe_json_dumps for invocation parameters in litellm instrumentor ([#1269](https://github.com/luke-moehlenbrock/openinference/issues/1269)) ([650dbb9](https://github.com/luke-moehlenbrock/openinference/commit/650dbb9f83ce7e94329d159819033d8f86e21129))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-groq: 0.1.12</summary>

## [0.1.12](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-groq-v0.1.11...python-openinference-instrumentation-groq-v0.1.12) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-instructor: 0.1.10</summary>

## [0.1.10](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-instructor-v0.1.9...python-openinference-instrumentation-instructor-v0.1.10) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* instructor output bug fix ([#1549](https://github.com/luke-moehlenbrock/openinference/issues/1549)) ([905325f](https://github.com/luke-moehlenbrock/openinference/commit/905325f324dd1d8079cebbb169b0b7fc933a8e0c))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-anthropic: 0.1.20</summary>

## [0.1.20](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-anthropic-v0.1.19...python-openinference-instrumentation-anthropic-v0.1.20) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* **anthropic:** add stream wrapper and tests ([#1572](https://github.com/luke-moehlenbrock/openinference/issues/1572)) ([918aa01](https://github.com/luke-moehlenbrock/openinference/commit/918aa017441fd4c8cffdbcaab287913349a41a60))
* **anthropic:** Added support for anthropic sdk input images rendering  ([#2091](https://github.com/luke-moehlenbrock/openinference/issues/2091)) ([d2684b4](https://github.com/luke-moehlenbrock/openinference/commit/d2684b4b20e3b0199051c553580a8b27b673727f))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* instrumentation-anthropic cache token counts ([#1465](https://github.com/luke-moehlenbrock/openinference/issues/1465)) ([d6765e0](https://github.com/luke-moehlenbrock/openinference/commit/d6765e0edd455fb879ccf0b58ea7d3dfaabeabf0))


### Bug Fixes

* include cache tokens in prompt tokens for anthropic ([#1429](https://github.com/luke-moehlenbrock/openinference/issues/1429)) ([abd36c4](https://github.com/luke-moehlenbrock/openinference/commit/abd36c45ea4ff966b58eccee42de252bc876d5ab))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-smolagents: 0.1.19</summary>

## [0.1.19](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-smolagents-v0.1.18...python-openinference-instrumentation-smolagents-v0.1.19) (2025-09-18)


### Features

* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))
* **smolagents:** add entrypoint for use in opentelemetry-instrument ([#1276](https://github.com/luke-moehlenbrock/openinference/issues/1276)) ([7d2af53](https://github.com/luke-moehlenbrock/openinference/commit/7d2af53fea2d3b7e03b20cbf056994fddc23d888))
* **smolagents:** Improve Display Of Handled Errors ([#1845](https://github.com/luke-moehlenbrock/openinference/issues/1845)) ([fb7eb1f](https://github.com/luke-moehlenbrock/openinference/commit/fb7eb1fa36adb7bb5ff001dce196c32ceb244a18))
* **smolagents:** support smolagents on python 3.13 ([#1294](https://github.com/luke-moehlenbrock/openinference/issues/1294)) ([415f57e](https://github.com/luke-moehlenbrock/openinference/commit/415f57e9cdcaf8ad4da8f73043f0fe8e64a7a1e0))
* **smolagents:** updates to latest and makes examples use opentelemetry-instrument ([#1277](https://github.com/luke-moehlenbrock/openinference/issues/1277)) ([b151bc9](https://github.com/luke-moehlenbrock/openinference/commit/b151bc9a3f8243c846c2981ade94e3d2823602e7))


### Bug Fixes

* allow prerelease versions of smolagents ([#1416](https://github.com/luke-moehlenbrock/openinference/issues/1416)) ([8cd680f](https://github.com/luke-moehlenbrock/openinference/commit/8cd680fcb4b7d88a1223f2e07bf1edb038021fac))
* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* only import exported smolagents models ([#1403](https://github.com/luke-moehlenbrock/openinference/issues/1403)) ([e175778](https://github.com/luke-moehlenbrock/openinference/commit/e175778252b0cd50d1d1fa20b53547fbf83f74cd))
* **smolagents:** Getting Multiple Traces While Streaming Code Agent ([#1872](https://github.com/luke-moehlenbrock/openinference/issues/1872)) ([420ea79](https://github.com/luke-moehlenbrock/openinference/commit/420ea79a5fd2ce572cb7bdcb38b6585107cce465))
* **smolagents:** include reasoning content ([#1697](https://github.com/luke-moehlenbrock/openinference/issues/1697)) ([0c8ea99](https://github.com/luke-moehlenbrock/openinference/commit/0c8ea99312874f605e1ab751e38dd13c8b0d4ea0))
* **smolagents:** instrument both __call__ and generate methods for complete model tracing ([#1744](https://github.com/luke-moehlenbrock/openinference/issues/1744)) ([a963b96](https://github.com/luke-moehlenbrock/openinference/commit/a963b9619776abe79fb6719eeb9eda01850aeff5))
* **smolagents:** Not Getting Step Spans From Latest Smolagents ([#2171](https://github.com/luke-moehlenbrock/openinference/issues/2171)) ([14f0a19](https://github.com/luke-moehlenbrock/openinference/commit/14f0a1994a43476f77b1e906912d4a572d194700))
* **smolagents:** prevent duplicate llm spans ([#2118](https://github.com/luke-moehlenbrock/openinference/issues/2118)) ([f1a2946](https://github.com/luke-moehlenbrock/openinference/commit/f1a29460344d37e7e431d2bd76bc6f724bcbb931))
* **smolagents:** support new managed agents ([#1274](https://github.com/luke-moehlenbrock/openinference/issues/1274)) ([306e1c5](https://github.com/luke-moehlenbrock/openinference/commit/306e1c5caf3827433c3a2151b93f7534533bbe94))
* **smolagents:** support smolagents nested llm input message contents ([#1238](https://github.com/luke-moehlenbrock/openinference/issues/1238)) ([51be5e4](https://github.com/luke-moehlenbrock/openinference/commit/51be5e47f4d5ae4ccf43d33a09c3475b56edf784))
* **smolagents:** use new token_usage structure ([#2087](https://github.com/luke-moehlenbrock/openinference/issues/2087)) ([c691712](https://github.com/luke-moehlenbrock/openinference/commit/c6917124a236eb6deff1e1faf214075662ebfc58))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-autogen: 0.1.10</summary>

## [0.1.10](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-autogen-v0.1.9...python-openinference-instrumentation-autogen-v0.1.10) (2025-09-18)


### Features

* add entrypoint for use in opentelemetry-instrument ([#1278](https://github.com/luke-moehlenbrock/openinference/issues/1278)) ([2106acf](https://github.com/luke-moehlenbrock/openinference/commit/2106acfd6648804abe9b95e41a49df26a500435c))
* define openinference_instrumentor entry points for all libraries ([#1290](https://github.com/luke-moehlenbrock/openinference/issues/1290)) ([4b69fdc](https://github.com/luke-moehlenbrock/openinference/commit/4b69fdc13210048009e51639b01e7c0c9550c9d1))


### Bug Fixes

* increased minimum supported version of openinference-instrumentation to 0.1.27 ([#1507](https://github.com/luke-moehlenbrock/openinference/issues/1507)) ([a55edfa](https://github.com/luke-moehlenbrock/openinference/commit/a55edfa8900c1f36a73385c7d03f91cffadd85c4))
* support python 3.13 and drop python 3.8 ([#1263](https://github.com/luke-moehlenbrock/openinference/issues/1263)) ([5bfaa90](https://github.com/luke-moehlenbrock/openinference/commit/5bfaa90d800a8f725b3ac7444d16972ed7821738))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))


### Documentation

* fix license to be openinference ([#1353](https://github.com/luke-moehlenbrock/openinference/issues/1353)) ([85d435b](https://github.com/luke-moehlenbrock/openinference/commit/85d435be3af3de5424494cfbdd654454688b7377))
</details>

<details><summary>python-openinference-instrumentation-beeai: 0.1.11</summary>

## [0.1.11](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-beeai-v0.1.10...python-openinference-instrumentation-beeai-v0.1.11) (2025-09-18)


### Features

* BeeAI Framework Updates ([#2060](https://github.com/luke-moehlenbrock/openinference/issues/2060)) ([720d1fe](https://github.com/luke-moehlenbrock/openinference/commit/720d1fe2db55fa95fa9721438b441c4f7924c726))
* beeai python package ([#1496](https://github.com/luke-moehlenbrock/openinference/issues/1496)) ([143b770](https://github.com/luke-moehlenbrock/openinference/commit/143b770500e615fb692b3e5f945e8dc22e69c1d1))
* **beeai:** updates so we can run 0.1.19 ([#1576](https://github.com/luke-moehlenbrock/openinference/issues/1576)) ([84129f0](https://github.com/luke-moehlenbrock/openinference/commit/84129f0212763c96e23961695c4915ec5d14f2f7))
* **python:** update beeai version ([#1552](https://github.com/luke-moehlenbrock/openinference/issues/1552)) ([48f04bb](https://github.com/luke-moehlenbrock/openinference/commit/48f04bb7fdd03525d7824d9889aebb745d012a5e))
* update BeeAI data serialization ([#2108](https://github.com/luke-moehlenbrock/openinference/issues/2108)) ([0994ec5](https://github.com/luke-moehlenbrock/openinference/commit/0994ec58ffbb905da975b5e0be5ea9b512ca528b))
* update beeai framework package ([#1525](https://github.com/luke-moehlenbrock/openinference/issues/1525)) ([dc8d128](https://github.com/luke-moehlenbrock/openinference/commit/dc8d128042c661babb75b2609bb2f97d155ae9d8))
* update beeai-framework integration ([#1829](https://github.com/luke-moehlenbrock/openinference/issues/1829)) ([c788ec3](https://github.com/luke-moehlenbrock/openinference/commit/c788ec3b8f1783fba1bb3d57022523d5de684b0a))


### Bug Fixes

* beeai python package ([#1522](https://github.com/luke-moehlenbrock/openinference/issues/1522)) ([36b50d7](https://github.com/luke-moehlenbrock/openinference/commit/36b50d7386f475a13a3665620b95cf4ade4e5ced))
* **beeaI:** dedupe traces/spans ([#2148](https://github.com/luke-moehlenbrock/openinference/issues/2148)) ([c528758](https://github.com/luke-moehlenbrock/openinference/commit/c5287584878089c4ea891b6768c5f2e4d86cbdb9))
* removes spurious print(2) from python beeai and converts rest to loggers ([#1560](https://github.com/luke-moehlenbrock/openinference/issues/1560)) ([038209a](https://github.com/luke-moehlenbrock/openinference/commit/038209ab6be0d95181db19c1ae15b244ec7afe0a))
* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))
</details>

<details><summary>python-openinference-instrumentation-portkey: 0.1.4</summary>

## [0.1.4](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-portkey-v0.1.3...python-openinference-instrumentation-portkey-v0.1.4) (2025-09-18)


### Features

* portkey chat completions ([#1495](https://github.com/luke-moehlenbrock/openinference/issues/1495)) ([0866af3](https://github.com/luke-moehlenbrock/openinference/commit/0866af3e9428f59c67704899da37a63cfbef453c))
* **portkey:** Add support for propmt template calls ([#1663](https://github.com/luke-moehlenbrock/openinference/issues/1663)) ([c1e813e](https://github.com/luke-moehlenbrock/openinference/commit/c1e813e26c62713229958c625c088ffe46ea1608))


### Bug Fixes

* update lower bound on openinference-semantic-conventions ([#1567](https://github.com/luke-moehlenbrock/openinference/issues/1567)) ([c2f428c](https://github.com/luke-moehlenbrock/openinference/commit/c2f428c5916c3dd62cf6670358f37111d4f7fd25))
</details>

<details><summary>python-openinference-instrumentation-mcp: 1.4.0</summary>

## [1.4.0](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-mcp-v1.3.1...python-openinference-instrumentation-mcp-v1.4.0) (2025-09-18)


### Features

* **mcp-python:** move instrumentation to transport layer ([#1563](https://github.com/luke-moehlenbrock/openinference/issues/1563)) ([2ef9208](https://github.com/luke-moehlenbrock/openinference/commit/2ef9208ecdf51e5cf5fba87da20f052ddb198668))
* **mcp:** add instrumentation support for Streamable-HTTP transport and bump mcp dependency to e1.8.1 ([#1640](https://github.com/luke-moehlenbrock/openinference/issues/1640)) ([4df8976](https://github.com/luke-moehlenbrock/openinference/commit/4df8976066f1911321ee31f7732854787079e981))
* **mcp:** mcp python context propagation ([#1524](https://github.com/luke-moehlenbrock/openinference/issues/1524)) ([1af5f7d](https://github.com/luke-moehlenbrock/openinference/commit/1af5f7d2e7c78e8fdebf9aaf2e50ccaa74eb6f9a))


### Bug Fixes

* **mcp:** handle ValidationError in stdio stream instrumentation ([#2170](https://github.com/luke-moehlenbrock/openinference/issues/2170)) ([48aa236](https://github.com/luke-moehlenbrock/openinference/commit/48aa2362a97a7efb029bd1f1e339297e6c6feec0))
* **mcp:** support mcp&gt;=1.8.0 with new SessionMessage structure ([#1634](https://github.com/luke-moehlenbrock/openinference/issues/1634)) ([ba6af47](https://github.com/luke-moehlenbrock/openinference/commit/ba6af477e97585a41f4a58efcb45890e9bb6c89c))
</details>

<details><summary>python-openinference-instrumentation-google-genai: 0.1.6</summary>

## [0.1.6](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-google-genai-v0.1.5...python-openinference-instrumentation-google-genai-v0.1.6) (2025-09-18)


### Features

* add Google GenAI instrumentation ([#1500](https://github.com/luke-moehlenbrock/openinference/issues/1500)) ([1e669a8](https://github.com/luke-moehlenbrock/openinference/commit/1e669a8af18bdfd8a0f92f716b49a7f6c105952a))
* Google Gen AI Tool Code Support ([#1763](https://github.com/luke-moehlenbrock/openinference/issues/1763)) ([ec5cc3f](https://github.com/luke-moehlenbrock/openinference/commit/ec5cc3f535cfb546f08506d18b93c373b494c7c2))


### Bug Fixes

* fix config_json serialization for GoogleGenAIInstrumentor ([#1855](https://github.com/luke-moehlenbrock/openinference/issues/1855)) ([1702a1d](https://github.com/luke-moehlenbrock/openinference/commit/1702a1d755d8ebc64fb3fa17e36579a6935d9dbd))
* google genai with pydantic ([#1724](https://github.com/luke-moehlenbrock/openinference/issues/1724)) ([e2ea09a](https://github.com/luke-moehlenbrock/openinference/commit/e2ea09a5395f47a5b60ec7961d22114293ebb4f1))
* include reasoning and audio token count for genai and adk instrumentors ([#1812](https://github.com/luke-moehlenbrock/openinference/issues/1812)) ([921ff07](https://github.com/luke-moehlenbrock/openinference/commit/921ff073e28ac2755b651dcdfac9ab3dbd673e70))


### Documentation

* fix google genai import in README ([#1605](https://github.com/luke-moehlenbrock/openinference/issues/1605)) ([60ee275](https://github.com/luke-moehlenbrock/openinference/commit/60ee2755fa99a68debbe5e9d84c25b92e99c5e31))
</details>

<details><summary>python-openinference-instrumentation-autogen-agentchat: 0.1.5</summary>

## [0.1.5](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-autogen-agentchat-v0.1.4...python-openinference-instrumentation-autogen-agentchat-v0.1.5) (2025-09-18)


### Features

* **autogen-agentchat:** add tool call semantic convention attributes ([#2104](https://github.com/luke-moehlenbrock/openinference/issues/2104)) ([fe0780d](https://github.com/luke-moehlenbrock/openinference/commit/fe0780d243e9ecf89e6548e5793c7265dede1b86))
* **autogen-agentchat:** auto instrumentation ([#1611](https://github.com/luke-moehlenbrock/openinference/issues/1611)) ([3c5857c](https://github.com/luke-moehlenbrock/openinference/commit/3c5857c2864c3b367888683d1fd470ec631c389f))
* **autogen-agentchat:** capture graph.node.id and graph.node.parent_id semantics ([#1867](https://github.com/luke-moehlenbrock/openinference/issues/1867)) ([9f8ca03](https://github.com/luke-moehlenbrock/openinference/commit/9f8ca0373856e94305e531ef1e325525b5958ff9))
* **autogen-agentchat:** instrumenting AssistantAgent, BaseOpenAIChatCompletionClient, and BaseGroupChat ([#1790](https://github.com/luke-moehlenbrock/openinference/issues/1790)) ([3a53ede](https://github.com/luke-moehlenbrock/openinference/commit/3a53ede8716e1a2d862ec653740b93881ebb1106))


### Bug Fixes

* **autogen-agentchat:** filter out invalid kwargs before binding calls and record new vcrs for tests for autogen version 0.6.x ([#1871](https://github.com/luke-moehlenbrock/openinference/issues/1871)) ([9c4ada0](https://github.com/luke-moehlenbrock/openinference/commit/9c4ada0847be85fff074ef493ad2f138f80369d2))
</details>

<details><summary>python-openinference-instrumentation-pydantic-ai: 0.1.6</summary>

## [0.1.6](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-pydantic-ai-v0.1.5...python-openinference-instrumentation-pydantic-ai-v0.1.6) (2025-09-18)


### Features

* pydanticai instrumentation ([#1639](https://github.com/luke-moehlenbrock/openinference/issues/1639)) ([d8c5b9c](https://github.com/luke-moehlenbrock/openinference/commit/d8c5b9cdf793dcce247b2ea852c28eba3a1989bc))
* update pydantic-ai to v2 tracing format ([#2186](https://github.com/luke-moehlenbrock/openinference/issues/2186)) ([5eecce5](https://github.com/luke-moehlenbrock/openinference/commit/5eecce5c648d710d3ad9397e23773096e5903352))


### Bug Fixes

* pydantic-ai fix span filtering ([#2016](https://github.com/luke-moehlenbrock/openinference/issues/2016)) ([c139f36](https://github.com/luke-moehlenbrock/openinference/commit/c139f3677233fb7c76b0b2bff5b4a2dafe1921dc))
* rename pydantic ai test dir ([#1706](https://github.com/luke-moehlenbrock/openinference/issues/1706)) ([d45b00c](https://github.com/luke-moehlenbrock/openinference/commit/d45b00cce1d5960e090dac3801a914523fb0355c))


### Documentation

* fix pip install in readme ([#1705](https://github.com/luke-moehlenbrock/openinference/issues/1705)) ([4fbad21](https://github.com/luke-moehlenbrock/openinference/commit/4fbad21f700325af4cd5d314881ec004a859bdf8))
</details>

<details><summary>python-openinference-instrumentation-google-adk: 0.1.5</summary>

## [0.1.5](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-google-adk-v0.1.4...python-openinference-instrumentation-google-adk-v0.1.5) (2025-09-18)


### Features

* add instrumentation for google-adk ([#1759](https://github.com/luke-moehlenbrock/openinference/issues/1759)) ([aeb1769](https://github.com/luke-moehlenbrock/openinference/commit/aeb17692d30cd8112bcad0990f1ec56491a59962))


### Bug Fixes

* **google-adk:** fix test compatibility with v1.13.0 ([#2176](https://github.com/luke-moehlenbrock/openinference/issues/2176)) ([dbe0668](https://github.com/luke-moehlenbrock/openinference/commit/dbe066844397be079e90900ab3eff9a920dbf436))
* include reasoning and audio token count for genai and adk instrumentors ([#1812](https://github.com/luke-moehlenbrock/openinference/issues/1812)) ([921ff07](https://github.com/luke-moehlenbrock/openinference/commit/921ff073e28ac2755b651dcdfac9ab3dbd673e70))
* pydantic model serialization for input value and image bytes for google-adk ([#2031](https://github.com/luke-moehlenbrock/openinference/issues/2031)) ([46ef152](https://github.com/luke-moehlenbrock/openinference/commit/46ef1522f73cf98f8c2b318b7afc7444160033b3))
* serialization of response schema in invocation parameters for google-adk ([#2033](https://github.com/luke-moehlenbrock/openinference/issues/2033)) ([586689f](https://github.com/luke-moehlenbrock/openinference/commit/586689f4ec6a37a6f3961740ebff4734f92ec3e5))
</details>

<details><summary>python-openinference-instrumentation-openlit: 0.1.3</summary>

## [0.1.3](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-openlit-v0.1.2...python-openinference-instrumentation-openlit-v0.1.3) (2025-09-18)


### Features

* Openlit span processor ([#2021](https://github.com/luke-moehlenbrock/openinference/issues/2021)) ([99c4c99](https://github.com/luke-moehlenbrock/openinference/commit/99c4c994b42486192bf07699ea6b75c3bd29efa1))
* Openlit span processor ([#2120](https://github.com/luke-moehlenbrock/openinference/issues/2120)) ([5280702](https://github.com/luke-moehlenbrock/openinference/commit/5280702ac7df30575eeb4bac416411f43c43ad8b))
* Openlit span processor ([#2127](https://github.com/luke-moehlenbrock/openinference/issues/2127)) ([a039137](https://github.com/luke-moehlenbrock/openinference/commit/a039137c99f4162963fab37359df04763310e001))
* **openlit:** implement span processor ([#2149](https://github.com/luke-moehlenbrock/openinference/issues/2149)) ([51689ae](https://github.com/luke-moehlenbrock/openinference/commit/51689aea3c41b513b22dcf3513389e91ec4c8f1e))
* **openlit:** openlit span processor ([#2151](https://github.com/luke-moehlenbrock/openinference/issues/2151)) ([013102e](https://github.com/luke-moehlenbrock/openinference/commit/013102e586ab0f8e441c6caec02c5b4c48bd5643))


### Bug Fixes

* fixing comments/file strings in openinference-instrumentation-openlit ([#2159](https://github.com/luke-moehlenbrock/openinference/issues/2159)) ([7a0a9d1](https://github.com/luke-moehlenbrock/openinference/commit/7a0a9d146aa2ce7f060e996c05b15b9dbbedb2fc))
</details>

<details><summary>python-openinference-instrumentation-openllmetry: 0.1.3</summary>

## [0.1.3](https://github.com/luke-moehlenbrock/openinference/compare/python-openinference-instrumentation-openllmetry-v0.1.2...python-openinference-instrumentation-openllmetry-v0.1.3) (2025-09-18)


### Features

* openinference-instrumentation-openllmetry (openllmetry converter) ([#1789](https://github.com/luke-moehlenbrock/openinference/issues/1789)) ([55fb98e](https://github.com/luke-moehlenbrock/openinference/commit/55fb98e8f23dd1d485a760e04496e0629bce6de0))
* Openlit span processor ([#2021](https://github.com/luke-moehlenbrock/openinference/issues/2021)) ([99c4c99](https://github.com/luke-moehlenbrock/openinference/commit/99c4c994b42486192bf07699ea6b75c3bd29efa1))
</details>

<details><summary>java-openinference-semantic-conventions: 0.1.10</summary>

## [0.1.10](https://github.com/luke-moehlenbrock/openinference/compare/java-openinference-semantic-conventions-v0.1.9...java-openinference-semantic-conventions-v0.1.10) (2025-09-18)


### Features

* Java release only, please ([#1881](https://github.com/luke-moehlenbrock/openinference/issues/1881)) ([0c75997](https://github.com/luke-moehlenbrock/openinference/commit/0c759977688c05a813a5121255f9da063aa9b4b0))
* **java:** add tool calling instrumentation, prepare dependabot PR ([#1901](https://github.com/luke-moehlenbrock/openinference/issues/1901)) ([33d3ded](https://github.com/luke-moehlenbrock/openinference/commit/33d3ded20fbd3097b4ee567c77d540526c480555))
* **langchain4j:** Java Openinference client, langchain4j example ([#1817](https://github.com/luke-moehlenbrock/openinference/issues/1817)) ([9ffb378](https://github.com/luke-moehlenbrock/openinference/commit/9ffb378c70396cb991136ebbeb8368eee493725d))
* new experimental release ([#2050](https://github.com/luke-moehlenbrock/openinference/issues/2050)) ([3afeed2](https://github.com/luke-moehlenbrock/openinference/commit/3afeed2d72d52a0d96217c9c1c6e1f7d3e983c73))
* Spring AI instrumentation, Java 17 update ([#2036](https://github.com/luke-moehlenbrock/openinference/issues/2036)) ([b260225](https://github.com/luke-moehlenbrock/openinference/commit/b2602255b7954296a70fa02b2c98d67c514d9b9f))
* Upgrade workflow java 17 ([#2044](https://github.com/luke-moehlenbrock/openinference/issues/2044)) ([2084e8e](https://github.com/luke-moehlenbrock/openinference/commit/2084e8e48761fbb9e575bf4fbfc0f75ba3998d2e))
* use generic updater markers ([#1887](https://github.com/luke-moehlenbrock/openinference/issues/1887)) ([ffda77a](https://github.com/luke-moehlenbrock/openinference/commit/ffda77a10970d8616cbf57a5565aeb5fc9aede9a))


### Bug Fixes

* bump java, add release-please gradle property ([#1875](https://github.com/luke-moehlenbrock/openinference/issues/1875)) ([8bd49ee](https://github.com/luke-moehlenbrock/openinference/commit/8bd49ee132c59974c1742fac309c5a91601dc45a))
* exclude java from python release path, read version from gradle.& ([#1877](https://github.com/luke-moehlenbrock/openinference/issues/1877)) ([f2a14bc](https://github.com/luke-moehlenbrock/openinference/commit/f2a14bc212491a01417eb08975be6ee0f9f99355))
* snapshot publish ([#1883](https://github.com/luke-moehlenbrock/openinference/issues/1883)) ([1c2532e](https://github.com/luke-moehlenbrock/openinference/commit/1c2532ecc2abb82c8bbdd87091a565dafd705756))
* SpringAI linking with correct dependencies ([#2098](https://github.com/luke-moehlenbrock/openinference/issues/2098)) ([8d944f8](https://github.com/luke-moehlenbrock/openinference/commit/8d944f8ab3b4b54ec449a256465128a7083d8e9e))
* typo on release ([#1884](https://github.com/luke-moehlenbrock/openinference/issues/1884)) ([5c2718e](https://github.com/luke-moehlenbrock/openinference/commit/5c2718e4dabff57be14f897ad8da23b03d208eab))
</details>

<details><summary>java-openinference-instrumentation: 0.1.8</summary>

## [0.1.8](https://github.com/luke-moehlenbrock/openinference/compare/java-openinference-instrumentation-v0.1.7...java-openinference-instrumentation-v0.1.8) (2025-09-18)


### Features

* add dependabot github action ([#1904](https://github.com/luke-moehlenbrock/openinference/issues/1904)) ([1283dfc](https://github.com/luke-moehlenbrock/openinference/commit/1283dfc3fcc9f728780f8c6a1ab865aa1f647a63))
* **langchain4j:** Java Openinference client, langchain4j example ([#1817](https://github.com/luke-moehlenbrock/openinference/issues/1817)) ([9ffb378](https://github.com/luke-moehlenbrock/openinference/commit/9ffb378c70396cb991136ebbeb8368eee493725d))
* new experimental release ([#2050](https://github.com/luke-moehlenbrock/openinference/issues/2050)) ([3afeed2](https://github.com/luke-moehlenbrock/openinference/commit/3afeed2d72d52a0d96217c9c1c6e1f7d3e983c73))
* Spring AI instrumentation, Java 17 update ([#2036](https://github.com/luke-moehlenbrock/openinference/issues/2036)) ([b260225](https://github.com/luke-moehlenbrock/openinference/commit/b2602255b7954296a70fa02b2c98d67c514d9b9f))
* Upgrade workflow java 17 ([#2044](https://github.com/luke-moehlenbrock/openinference/issues/2044)) ([2084e8e](https://github.com/luke-moehlenbrock/openinference/commit/2084e8e48761fbb9e575bf4fbfc0f75ba3998d2e))
* use generic updater markers ([#1887](https://github.com/luke-moehlenbrock/openinference/issues/1887)) ([ffda77a](https://github.com/luke-moehlenbrock/openinference/commit/ffda77a10970d8616cbf57a5565aeb5fc9aede9a))


### Bug Fixes

* bump java, add release-please gradle property ([#1875](https://github.com/luke-moehlenbrock/openinference/issues/1875)) ([8bd49ee](https://github.com/luke-moehlenbrock/openinference/commit/8bd49ee132c59974c1742fac309c5a91601dc45a))
* SpringAI linking with correct dependencies ([#2098](https://github.com/luke-moehlenbrock/openinference/issues/2098)) ([8d944f8](https://github.com/luke-moehlenbrock/openinference/commit/8d944f8ab3b4b54ec449a256465128a7083d8e9e))
</details>

<details><summary>java-openinference-instrumentation-langchain4j: 0.1.6</summary>

## [0.1.6](https://github.com/luke-moehlenbrock/openinference/compare/java-openinference-instrumentation-langchain4j-v0.1.5...java-openinference-instrumentation-langchain4j-v0.1.6) (2025-09-18)


### Features

* **java:** add tool calling instrumentation, prepare dependabot PR ([#1901](https://github.com/luke-moehlenbrock/openinference/issues/1901)) ([33d3ded](https://github.com/luke-moehlenbrock/openinference/commit/33d3ded20fbd3097b4ee567c77d540526c480555))
* **langchain4j:** Java Openinference client, langchain4j example ([#1817](https://github.com/luke-moehlenbrock/openinference/issues/1817)) ([9ffb378](https://github.com/luke-moehlenbrock/openinference/commit/9ffb378c70396cb991136ebbeb8368eee493725d))
* new experimental release ([#2050](https://github.com/luke-moehlenbrock/openinference/issues/2050)) ([3afeed2](https://github.com/luke-moehlenbrock/openinference/commit/3afeed2d72d52a0d96217c9c1c6e1f7d3e983c73))
* Spring AI instrumentation, Java 17 update ([#2036](https://github.com/luke-moehlenbrock/openinference/issues/2036)) ([b260225](https://github.com/luke-moehlenbrock/openinference/commit/b2602255b7954296a70fa02b2c98d67c514d9b9f))
* Upgrade workflow java 17 ([#2044](https://github.com/luke-moehlenbrock/openinference/issues/2044)) ([2084e8e](https://github.com/luke-moehlenbrock/openinference/commit/2084e8e48761fbb9e575bf4fbfc0f75ba3998d2e))
* use generic updater markers ([#1887](https://github.com/luke-moehlenbrock/openinference/issues/1887)) ([ffda77a](https://github.com/luke-moehlenbrock/openinference/commit/ffda77a10970d8616cbf57a5565aeb5fc9aede9a))


### Bug Fixes

* bump java, add release-please gradle property ([#1875](https://github.com/luke-moehlenbrock/openinference/issues/1875)) ([8bd49ee](https://github.com/luke-moehlenbrock/openinference/commit/8bd49ee132c59974c1742fac309c5a91601dc45a))
</details>

<details><summary>java-openinference-instrumentation-springAI: 0.1.8</summary>

## [0.1.8](https://github.com/luke-moehlenbrock/openinference/compare/java-openinference-instrumentation-springAI-v0.1.7...java-openinference-instrumentation-springAI-v0.1.8) (2025-09-18)


### Features

* new experimental release ([#2050](https://github.com/luke-moehlenbrock/openinference/issues/2050)) ([3afeed2](https://github.com/luke-moehlenbrock/openinference/commit/3afeed2d72d52a0d96217c9c1c6e1f7d3e983c73))
* Spring AI instrumentation, Java 17 update ([#2036](https://github.com/luke-moehlenbrock/openinference/issues/2036)) ([b260225](https://github.com/luke-moehlenbrock/openinference/commit/b2602255b7954296a70fa02b2c98d67c514d9b9f))
* Upgrade workflow java 17 ([#2044](https://github.com/luke-moehlenbrock/openinference/issues/2044)) ([2084e8e](https://github.com/luke-moehlenbrock/openinference/commit/2084e8e48761fbb9e575bf4fbfc0f75ba3998d2e))


### Bug Fixes

* jreleaser dependency release, all packages need their version ([#2075](https://github.com/luke-moehlenbrock/openinference/issues/2075)) ([5a2de93](https://github.com/luke-moehlenbrock/openinference/commit/5a2de939136b2d151a831e8911a62a0c3f7b7717))
* SpringAI linking with correct dependencies ([#2098](https://github.com/luke-moehlenbrock/openinference/issues/2098)) ([8d944f8](https://github.com/luke-moehlenbrock/openinference/commit/8d944f8ab3b4b54ec449a256465128a7083d8e9e))
* SpringAI multiple output messages ([#2106](https://github.com/luke-moehlenbrock/openinference/issues/2106)) ([3c5fd97](https://github.com/luke-moehlenbrock/openinference/commit/3c5fd97ed045a36dd95d4689a8b5315b95ee6366))
* trigger springAI release ([#2061](https://github.com/luke-moehlenbrock/openinference/issues/2061)) ([e97f324](https://github.com/luke-moehlenbrock/openinference/commit/e97f324ca8a12d788148edd9a031fabfe7055e55))
</details>

---
This PR was generated with [Release Please](https://github.com/googleapis/release-please). See [documentation](https://github.com/googleapis/release-please#release-please).