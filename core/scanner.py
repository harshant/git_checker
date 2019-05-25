import requests
from threading import Thread
from core import colors

git_paths = [
    ".git",
    ".git/",
    ".git/branches/",
    ".git/COMMIT_EDITMSG",
    ".git/config",
    ".git/configf",
    ".git/description",
    ".git/FETCH_HEAD",
    ".git/HEAD",
    ".git/hooks/",
    ".git/index",
    ".git/info/",
    ".git/info/exclude",
    ".git/logs/",
    ".git/logs/HEAD",
    ".git/logs/refs",
    ".git/logs/refs/heads",
    ".git/logs/refs/heads/master",
    ".git/logs/refs/remotes",
    ".git/logs/refs/remotes/origin",
    ".git/logs/refs/remotes/origin/HEAD",
    ".git/logs/refs/remotes/origin/master",
    ".git/objects/",
    ".git/packed-refs",
    ".git/refs/",
    ".git/refs/heads",
    ".git/refs/heads/master",
    ".git/refs/remotes",
    ".git/refs/remotes/origin",
    ".git/refs/remotes/origin/HEAD",
    ".git/refs/remotes/origin/master",
    ".git/refs/tags",
]


class Scan:
    def __init__(self, args_obj, base_path):
        self.arg_obj = args_obj
        self.base_path = base_path
        self.threads = []

        if args_obj.args.input:
            with open(base_path + "/" + args_obj.args.input) as self.domain_file:
                self.domain_list = self.domain_file.read().split("\n")
                self.domain_file.close()

                while "" in self.domain_list:
                    self.domain_list.remove("")  # remove any blank line in the file

                for domain in self.domain_list:
                    if domain.find("https://") >= 0 or domain.find("http://") >= 0:
                        self.scan(domain)
                    else:
                        self.scan("http://" + domain)

    def scan(self, domain):
        self.domain = domain
        self.check = True

        if self.domain.endswith("/"):
            self.domain = self.domain[:-1]  # removing trailing "/" if any
        print(colors.info + "Checking : " + self.domain)

        for self.path in git_paths:
            self.create_thread(self.domain, self.path)
        for self.process in self.threads:
            self.process.join()

        if self.check:
            print(colors.bad + "Not vulnerable to .git misconfiguration")
        print(
            colors.green
            + "=================================================================="
        )

    def create_thread(self, domain, path):
        self.domain = domain
        self.path = path
        self.process = Thread(target=self.requester, args=[self.domain, self.path])
        self.process.start()
        self.threads.append(self.process)

    def requester(self, domain, path):
        self.domain = domain
        self.path = path
        try:
            self.response_code = requests.get(
                self.domain + "/" + self.path, timeout=5
            ).status_code
            if self.response_code == 200:
                print(
                    colors.good + colors.white + "found : " + self.domain + "/" + path
                )
                self.check = False
        except:
            self.check = False
            print(
                colors.bad
                + colors.white
                + "Can not connect to url : "
                + self.domain
                + "/"
                + path
            )
