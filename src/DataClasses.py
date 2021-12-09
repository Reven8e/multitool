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
