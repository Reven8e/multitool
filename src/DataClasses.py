from dataclasses import dataclass, field

@dataclass
class boganBusterData:
    thr: int = field(default=int)
    target: str= field(default=str)
    wordlist_path: str= field(default=str)
    proxylist_path: str = field(default=str)
    proxy_type: str = field(default=str)
    good_dirs: list = field(default_factory=list)
    proxylist: list = field(default_factory=list)
    wordlist: list = field(default_factory=list)


@dataclass
class porxyCheckerData:
    thr: int = field(default_factory=int)
    proxylist: list = field(default_factory=list)
    proxy_type: str = field(default_factory=str)
    good_proxies: list = field(default_factory=list)


@dataclass
class sshBruteData:
    thr: int = field(default=int)
    timeout: float = field(default=float)
    target: str = field(default=str)
    check_type: str = field(default=str)
    wordlist_usernames_path: str = field(default=str)
    wordlist_usernames: list = field(default=list)
    wordlist_passwords_path: str= field(default=str)
    wordlist_passwords: list = field(default=list)
    goods: list = field(default_factory=list)
