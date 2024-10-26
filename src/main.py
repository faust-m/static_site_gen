import os
import shutil
from blocks import markdown_to_blocks, markdown_to_html_node


def copy_contents(src_dir, dst_dir, clean_dir=False):
    if os.path.exists(dst_dir) and clean_dir:
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    src_files = os.listdir(src_dir)
    for item in src_files:
        src_path = os.path.join(src_dir, item)
        if os.path.isfile(src_path):
            dst_path = os.path.join(dst_dir, item)
            print(f"Copying {src_path} to {dst_path}...")
            shutil.copy(src_path, dst_path)
        else:
            dst_path = os.path.join(dst_dir, item)
            copy_contents(src_path, dst_path)



def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    h_value = len(blocks[0]) - len(blocks[0].lstrip("#"))
    if h_value != 1:
        raise Exception("No title header found")
    return blocks[0].lstrip("#").strip()



def generate_page(from_path, template_path, dest_path):
    with open(from_path) as md_file:
        markdown = md_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dest_path = dest_path.replace(".md", ".html")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(dest_path, 'w') as out_file:
        out_file.write(template)
    


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    items = os.listdir(dir_path_content)
    for item in items:
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, dest_path)
        else:
            generate_pages_recursive(content_path, template_path, dest_path)



def main():
    copy_contents("./static/", "./public/", True)
    generate_pages_recursive("./content/", "template.html", "./public/")



if __name__ == "__main__":
    main()