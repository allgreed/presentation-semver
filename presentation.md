<!-- todo: update git remote -->
# Semver - how to avoid dependency hell
## by Olgierd &#34;Allgreed&#34; Kasprowicz


## $$$
<img style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/just.png">


# <span style="color: #b58900">Disclaimer</span>
<!-- .slide: data-background-color="black" -->

### source: github.com/allgreed/presentation-semver

Note:
- Prezka jest open source, kod na Githubie, linki w niej działają ;D
- Moje opinie są moje, a nie mojego pracodawcy lub podmiotów, w których jestem udziałowcem.

- (...) Nie będzie nic o Pypi - nie zdążyłem zrobić dobrego researchu

- Pytania wyjaśniające: w trakcie, pytania prowokujące shitstorm: po prezce - Niech ludzie, którzy tego nie znają się czegoś nauczą, a potem możemy pośmieszkować

- Zbieram feedback - jak ktoś uważa, że moją prezentację można poprawić to dawać znaki po prezkach / na Slacku



## Dependency hell?

[Technopedia](https://www.techopedia.com/definition/27701/dependency-hell):
> "Dependency hell is a term used to define the problems faced by software developers, publishers and users in general, when software or a software package is dependent on other software. ...[it] occurs when software works abnormally or displays errors and bugs due to an integrated software/application developed by a third party."</div>

Note: To nie jest precyzyjny termin, jest sporo definicji
My definition: When you update your dependencies, code breaks and you're in hell



## Let's play a game

### <span class="fragment fade-up" data-fragment-index="1"><img height=50 width=50 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">2?</span> <span class="fragment fade-up" data-fragment-index="2"><img height=50 width=50 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">3?</span>

```
print "spam"
```
<!-- .element: class="fragment fade-left" data-fragment-index="3" -->

```
for i in range(1):
    print("spam")
```
<!-- .element: class="fragment fade-right" data-fragment-index="4" -->

```
    int(str(3 / 2))
```
<!-- .element: class="fragment fade-left" data-fragment-index="5" -->

Note: Will this work in Python 2? Will this work in Python 3?


## Meh, let's play a better game!

<span class="fragment fade-up" data-fragment-index="1">- <img height=80 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/package.png"></span>
<br>
<span class="fragment fade-up" data-fragment-index="2">- <img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">2.6</span>

<div class="fragment fade-up" data-fragment-index="3">
- <img height=70 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pypy.png">
<img height=70 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/jython.png">
</div>

<br>
<span class="fragment fade-left" data-fragment-index="4"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">3?</span> 
<span class="fragment fade-right" data-fragment-index="5"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">2.7?</span> 
<span class="fragment fade-left" data-fragment-index="6"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">2.6.1?</span> 

Note: Arbitralna paczka, działa w wersji 2.6 Cpythona, działa również w pozostałych interpreterach (w odpowiedniej wersji) [Ergo: nie wykorzystuje specyfiki implementacji konkretnego interpretera]. Czy będzie działać pod tymi Pythonami? W sumie meh, bo można sprawdzić - te interpretery istnieją.


## Even moar!

<span class="fragment fade-up" data-fragment-index="1">- <img height=80 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/package.png"></span>
<br>
<span class="fragment fade-up" data-fragment-index="2">- <img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">8.2</span>

<div class="fragment fade-up" data-fragment-index="3">
- <img height=70 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pypy.png">
<img height=70 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/jython.png">
</div>

<br>
<span class="fragment fade-left" data-fragment-index="4"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">9?</span> 
<span class="fragment fade-right" data-fragment-index="5"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">8.5?</span> 
<span class="fragment fade-left" data-fragment-index="6"><img height=30 width=30 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/pytong.png">8.2.87?</span> 



## I had a dream

<img width=200 style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/contract.png">
- Improvements and security patches - not breaking current code
- Like never!
- ↑ can be reliably automated

Note: Kontrakt między twórcami, a userami => przyszłość - można wnioskować pewne rzeczy o paczkach, które nie istnieją (jeszcze). Możliwe są automatyczne update'y bez strachu o działanie kodu.



## [Semver 2.0.0](https://semver.org/) versioning scheme

- Clearly defined public API

- Releases are immutable

- Version consists of:
    - Major (<span style="color: #b58900">3</span>.6.1)
    - Minor (3.<span style="color: #b58900">6</span>.1)
    - Patch (3.6.<span style="color: #b58900">1</span>)

Note: Tom Preston-Werner / 1.0.0 - 2011


## But how???
- Major (2.x.y -> <span style="color: #b58900">3</span>.6.1) == lots of new stuff
- Minor (3.5.y -> 3.<span style="color: #b58900">6</span>.1) == new compatible stuff
- Patch (3.6.0 -> 3.6.<span style="color: #b58900">1</span>) == current stuff but better

Note: Ok, sounds good - how to version? The version doesn't mean anything on it's own. It has to be compared. Major == API may break, patches also include security fatches, fixes, optimization improvements. It's not about how big is the change -> it's about how much it affects the API.


# Demo


## Is Python under semver?

Claim:
<img style="margin: 0; box-shadow: none; border: 0; background: transparent" src="/img/claim.png">

1. [Clearly defined public API](https://docs.python.org/3/)
2. [Major, minor, patch](https://www.python.org/dev/peps/pep-0006/)
3. Ever heard of changing package contents?

But:
[Preleases](https://github.com/python/cpython/releases)

Note: Wycinek z krytyki semvera. Technicznie nie, bo w prereleasach powinien być "+", ale sami oceńcie


## What if?

- Rapid changes?
    - 0.x.y

- Move fast and break things?
    - Prereleases

- Releasing breaking changes by accident?
    - [RTFM](https://semver.org/#faq)



## Common sense applies
<img src="/img/reset.jpg">

Note: Resetting the counter - It's all about the end user - if there's no consumer there's no contract to be broaken


## Criticism

- Huge breaking updates <- Small incremental changes 
- [It's unreallistic in current - "allways on" environement](https://surfingthe.cloud/semantic-versioning-anti-pattern/)
- ["Romantic versioning" - every change is a breaking change](https://gist.github.com/jashkenas/cbd2b088e20279ae2c8e)

Note:
- W niektórych projektach lepiej jest update'ować kawałek po kawałku, zamiast takich wielkich kobył
- Problem leży gdzie indziej i tam go trzeba rozwiązywać
- Autor uważa że jest w ogóle bullshit


## When not to use semver

- Window apps
- Webistes ?
- CLIs ???

In general:
- **Not** dependencies 

Note: No chyba, że jest to przeznaczone do użytku maszynowego, np. skryptowalne CLI, crawlowalne strony, klilakne aplikacje okienkowe???


## Podziękował!


# Shitstorm? :)

