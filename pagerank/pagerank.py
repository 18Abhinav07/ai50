import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    pages_list = list(corpus.keys())
    total_pages = len(pages_list)

    # probability when random page chosen
    prob_random = (1 - damping_factor) * (1 / total_pages)
    # if we have no links that this current page connects to then we
    # have to give prob of page present = 0 else we will have it as:
    linked_pages = corpus[page]
    prob_present_in_links = (0 if len(linked_pages) == 0 else (1 / len(linked_pages)) * damping_factor)

    P_dist = {itr_page: prob_present_in_links + prob_random if itr_page in linked_pages else prob_random for itr_page in
              pages_list}
    return P_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    assert n > 0
    sample = random.choice(list(corpus.keys()))
    cur_sample_dist = {}  # to maintain the current number of visits.

    for i in range(0, n):
        p_dist = transition_model(corpus, sample, damping_factor)
        pages_in_model = list(p_dist.keys())
        pages_probability = list(p_dist.values())
        sample = random.choices(population=pages_in_model, weights=pages_probability)[0]
        cur_sample_dist[sample] = cur_sample_dist.get(sample, 0) + 1

    final_dist_rank = {page: (visits / n) for page, visits in cur_sample_dist.items()}
    return final_dist_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pages = list(corpus.keys())
    total_pages = len(pages)
    dist_rank = {page: (1 / total_pages) for page in pages}
    altered_rank = {}

    # check for every page : count the number of times the page occurs as a link
    # in other pages.

    itr = True
    while itr:
        for page_to_check in pages:
            new_rank = 0
            for linked_page in corpus:
                if page_to_check in corpus[linked_page]:
                    # we have this page as a link in the linked_page
                    new_rank += dist_rank[linked_page] / len(corpus[linked_page])
                if not corpus[linked_page]:  # if the linked_page has no links to any page.
                    new_rank += dist_rank[linked_page] / total_pages  # assumed to have link to all pages

            altered_rank[page_to_check] = (1 - damping_factor) / total_pages + new_rank * damping_factor
            # above used is the pr formula.

        for page in dist_rank:
            if abs(altered_rank[page] - dist_rank[page]) < 0.001:
                itr = False
            else:
                itr = True
            dist_rank[page] = altered_rank[page]

    return dist_rank


if __name__ == "__main__":
    main()
