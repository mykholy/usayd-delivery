import subprocess
import json
import sys

def get_pr_data(repo, pr_num):
    print(f"==================================================")
    print(f"=== {repo} PR #{pr_num} ===")
    print(f"==================================================")
    
    # 1. PR details
    res = subprocess.run([
        'gh', 'pr', 'view', str(pr_num),
        '--repo', repo,
        '--json', 'number,title,baseRefName,headRefName,headRefOid,state,reviews,comments'
    ], capture_output=True, text=True, encoding='utf-8')
    
    if res.returncode == 0:
        data = json.loads(res.stdout)
        title = data.get('title')
        base = data.get('baseRefName')
        head = data.get('headRefName')
        head_oid = data.get('headRefOid', '')[:7]
        print(f"Title: {title} | Base: {base} | Head: {head} ({head_oid})")
        
        # Reviews
        reviews = data.get('reviews', [])
        print(f"Reviews count: {len(reviews)}")
        for r in reviews:
            author = r.get('author', {}).get('login', 'unknown')
            state = r.get('state')
            submitted = r.get('submittedAt')
            body = r.get('body', '').strip()
            print(f"  Review by {author}: {state} at {submitted}")
            if body:
                print(f"    Body:\n{body}\n")
                
        # Issue comments
        comments = data.get('comments', [])
        print(f"Issue Comments count: {len(comments)}")
        for c in comments:
            author = c.get('author', {}).get('login', 'unknown')
            body = c.get('body', '').strip()
            print(f"  Comment by {author}:\n{body}\n")
            
    # Also fetch review comments (inline comments on diff)
    res_rc = subprocess.run([
        'gh', 'api', f'repos/{repo}/pulls/{pr_num}/comments'
    ], capture_output=True, text=True, encoding='utf-8')
    
    if res_rc.returncode == 0:
        rcs = json.loads(res_rc.stdout)
        print(f"Inline diff comments count: {len(rcs)}")
        for rc in rcs:
            path = rc.get('path')
            line = rc.get('line')
            user = rc.get('user', {}).get('login')
            body = rc.get('body', '').strip()
            print(f"  [{path}:{line}] by {user}:\n{body}\n")
    print()

if __name__ == '__main__':
    targets = [
        ('mykholy/usayd-api', p) for p in range(2, 12)
    ] + [
        ('mykholy/usayd-flutter', p) for p in range(1, 7)
    ]
    
    for repo, pr_num in targets:
        get_pr_data(repo, pr_num)
