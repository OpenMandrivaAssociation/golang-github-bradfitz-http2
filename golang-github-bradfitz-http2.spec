# http://github.com/bradfitz/http2
%global goipath         github.com/bradfitz/http2
%global commit          aa7658c0e9902e929a9ed0996ef949e59fc0f3ab

%gometa

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        HTTP/2 support for Go (in active development)
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
files="$(find . -iname 'testdata' -type d)"
%goinstall $files glide.lock glide.yaml

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README AUTHORS CONTRIBUTORS

%changelog
* Tue Nov 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20181113gitaa7658c
- Bump to commit aa7658c0e9902e929a9ed0996ef949e59fc0f3ab

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.13.20150509gitf8202bc
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20150509gitf8202bc
- Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150509gitf8202bc
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitf8202bc
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf8202bc
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf8202bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitf8202bc
- Update to spec-2.1
  related: #1246033

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf8202bc
- First package for Fedora
  resolves: #1246033

