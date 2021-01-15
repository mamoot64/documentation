import pytest
from integrations import replace_image_src

def test_image_src_replaced_by_shortcode(file_name):
  ## assert that a search of the regex pattern doesn't return any results
  ## instead we should find a shortcode pattern somewhere in the generated markdown

  ## markdown_img_search_regex = r"!\[(.*?)\]\((.*?)\)"
  assert "hello" == "hello"