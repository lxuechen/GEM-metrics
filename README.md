GEM-metrics
===========
Automatic metrics for GEM benchmark tasks. Can also be used standalone for evaluation of various natural language
generation tasks.

Installation
------------

GEM-metrics require recent Python 3, virtualenv or similar is recommended. To install, simply run:

```
git clone https://github.com/GEM-benchmark/GEM-metrics
cd GEM-metrics
pip install -r requirements.txt -r requirements-heavy.txt
```

If you want to just run the metrics from console (and don't need access to the checkout), you can just run:

```
pip install 'gem-metrics[heavy] @ git+https://github.com/GEM-benchmark/GEM-metrics.git'
```

Note that some NLTK stuff may be downloaded upon first run into a subdirectory where the code is located, so make sure
you have write access when you run this. Also note that all the required Python libraries are around 3 GB in size when
installed.

If you don't need trained metrics (BLEURT, BERTScore, NUBIA, QuestEval), you can ignore the “heavy” part, i.e. only
install dependencies from `requirements.txt` or only use `gem-metrics` instead of `gem-metrics[heavy]`
if installing without checkout. That way, your installed libraries will be ~300 MB.

Usage
-----

To compute all default metrics for a file, run:

```
<script> [-r references.json] outputs.json
```

Where `<script>` is either `./run_metrics.py` (if you created a checkout) or `gem_metrics` if you installed directly
via `pip`.

See [`test_data`](test_data/) for example JSON file formats.

Use `./run_metrics.py -h` to see all available options.

By default, the “heavy” metrics (BERTScore, BLEURT, NUBIA and QuestEval) aren't computed. Use `--heavy-metrics` to
compute them.

To run the example:

```bash
./run_metrics.py -r ./test_data/single_dataset.refs.json ./test_data/single_dataset.outs.json \
  --metric-list bleu meteor rouge nist bertscore bleurt
```

License
-------
Licensed under [the MIT license](LICENSE).
