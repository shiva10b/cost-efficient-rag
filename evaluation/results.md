# Evaluation Results

## Test Questions

1. What is Artificial Intelligence?
2. What is Machine Learning?

---

## Retrieval Performance

| Metric                       | Value |
| ---------------------------- | ----: |
| Top-K                        |     5 |
| Retrieved Documents          |     2 |
| Relevant Documents Retrieved |     2 |
| Hit Rate                     |  100% |
| Recall@5                     |  100% |
| MRR                          |  1.00 |
| nDCG@5                       |  1.00 |

---

## Latency

Average retrieval latency observed during testing:

* Approximately 0.5–1.0 seconds per query on a local machine.

---

## Observations

* Both evaluation queries successfully retrieved the expected document chunks.
* Retrieved contexts were relevant to the user questions.
* The generated answers were grounded in the retrieved documents.
* No hallucinated information was observed for the tested examples.

---

## Conclusion

The retrieval pipeline demonstrated high accuracy on the evaluation dataset, with all relevant documents retrieved within the configured Top-K results. The system provided grounded responses while maintaining low latency suitable for local deployment.
