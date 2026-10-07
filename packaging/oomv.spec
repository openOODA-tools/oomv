Name:           oomv
Version:        0.1.0
Release:        1%{?dist}
Summary:        Atomic directory and file mover across partitions with rollback on copy failure.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomv
Source0:        oomv-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomv is a sovereign, capability-bounded ATOMIC MOVER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomv
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomv-uninstall

%files
/usr/bin/oomv
/usr/bin/oomv-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
