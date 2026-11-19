# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 43 (printed ٤٢)."""

PAGE_NUMBER = 43
PRINTED_PAGE = "٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "يستلزم الدلالة. فهي: (إما) من صفتها: (أن تدل على معنى)[[١]] كائن (في نفسها) أي: في نفس الكلمة.",
     "en": "…entails signification (dalāla). So it [the word] is: (either) — among its attributes — (that it signifies a meaning) subsisting (in itself), that is: in the word itself."},
    {"type": "matn",
     "ar": "والمراد بكون المعنى في نفسها: أن تدل عليه بنفسها، من غير حاجة إلى انضمام كلمة أخرى[[٢]] إليها لاستقلاله بالمفهومية.",
     "en": "What is meant by the meaning being “in itself” is that it signifies it by itself, without need of adjoining another word to it, owing to its independence in conceptual signification (mafhūmiyya)."},
    {"type": "matn",
     "ar": "(أو) من صفتها: (أن لا) تدل على معنى في نفسها، بل تدل على معنى تحتاج في الدلالة عليه إلى انضمام كلمة أخرى إليها، لعدم استقلاله بالمفهومية.",
     "en": "(Or) — among its attributes — (that it does not) signify a meaning in itself; rather it signifies a meaning for whose signification it requires another word to be adjoined to it, owing to its lack of independence in conceptual signification."},
    {"type": "matn",
     "ar": "وسيجيء تحقيق ذلك في بيان حد الاسم إن شاء الله تعالى.",
     "en": "The verification of this will come in the exposition of the definition of the noun (ism), Allah the Exalted willing."},
    {"type": "matn",
     "ar": "القسم (الثاني): وهو ما لا يدل على معنى في نفسها (الحرف)[[٣]] كـ«من»، و«إلى»،",
     "en": "The (second) category — which is that which does not signify a meaning in itself — is (the particle, al-ḥarf), such as “min” (from) and “ilā” (to);"},
    {"type": "matn",
     "ar": "فإنهما يحتاجان في الدلالة على معنييهما، أعني: الابتداء والانتهاء[[٤]] إلى كلمة أخرى، كـ«البصرة والكوفة» في قوله: «سرت من البصرة إلى الكوفة»[[٥]].",
     "en": "for the two of them require, in signifying their two meanings — namely, origination (ibtidāʾ) and termination (intihāʾ) — another word, such as “al-Baṣra” and “al-Kūfa” in one’s saying: “I travelled from al-Baṣra to al-Kūfa.”"},
    {"type": "matn",
     "ar": "وإنما سمي هذا",
     "en": "And this [category] was so named only…"},  # continues on the next page

    {"type": "rule"},

    # ---------------- Orphan continuation (tail of a footnote from p.42) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "يقدرون عامل الظرف في نظم الكلام. وعبارة الشرح يحتملهما.",
     "en": "…they estimate the governing element of the adverbial (ẓarf) in the syntactic arrangement of the speech; and the wording of the Sharḥ admits of both."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: التقدير هكذا؛ لأن حالها، أو دلالتها، أو لأنها إما ذات دلالة. ولا يخفى أن تقدير الشرح مما يقبله الطبع السليم غاية القبول.",
     "en": "It has been said: the implied estimation (taqdīr) is thus — because [what is at issue is] its state (ḥāl), or its signification (dalāla), or because it is a thing possessing signification. It is not hidden that the estimation of the Sharḥ is such as the sound natural disposition accepts in the fullest measure."},
    {"type": "pair",
     "ar": "أما تقدير الحال والدلالة فلا يناسب مقام تقسيم الكلمة، ولا القول بأن الثاني حرف، والأول اسم أو فعل. ويستدعي عدم صحة الحصر على الأول، وعدم صحة الحمل على الثاني؛",
     "en": "As for estimating [it as] “state” (ḥāl) and “signification” (dalāla), that does not suit the context of dividing the word (kalima), nor [does] the statement that the second is a particle and the first a noun or a verb. And it entails the invalidity of the exclusive restriction (ḥaṣr) upon the first, and the invalidity of predication upon the second;"},
    {"type": "pair",
     "ar": "لأن حال الكلمة لا تنحصر في الدلالة وعدمها، ودلالتها لا يصح حمل عدم الدلالة عليها مع أن الضرورة التي دعت إلى التقدير إنما نشأت من الثاني، فالأليق التأويل فيه لا في الأول.",
     "en": "because the state of the word is not restricted to signification and its absence, and as for “its signification,” it is not valid to predicate the absence of signification of it — together with [the fact] that the necessity (ḍarūra) that called for the estimation arose only from the second; so what is more fitting is that interpretation (taʾwīl) be in it, not in the first."},
    {"type": "pair",
     "ar": "وأما تقدير الذات فيخالف ما اقتضاه زيادة «أن»، وكذا جعل «أن يدل» بمعنى الدال.",
     "en": "As for estimating [it as] “essence” (dhāt), that contradicts what the addition of “an” requires; and likewise making “an yadulla” mean “the signifier” (al-dāll)."},
    {"type": "pair",
     "ar": "التقدير في هذا المقام مبني على ما حكموا به من أن الفعل مع «أن» في تأويل المصدر. ولو وضع هناك المصدر بدله احتيج إلى ما ذكر، لكن النظر إلى المعنى يغني عنه؛ إذ ليس في معنى المصدر حقيقة، ولا يخلو من خدشة.",
     "en": "The estimation in this context is built upon what they have ruled: that the verb together with “an” stands in the interpretation of the verbal noun (maṣdar). And had the verbal noun been placed there in its stead, recourse to what was mentioned would be needed; but consideration of the meaning dispenses with it, since there is nothing in the meaning of the verbal noun in reality — and it is not free of a flaw (khadsha)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مفردا أو مركبا إليها.",
     "en": "Whether single (mufrad) or compound (murakkab), [is what is adjoined] to it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "استئناف؛ لأنه لما قال: إما كذا أو كذا، كأن سائلا قال: ما الأول وما الثاني؟ فقال: الثاني الحرف، والأول إما كذا أو كذا، معطوفا على الجملة الاستئنافية.",
     "en": "[It is] a resumption (istiʾnāf); for when he said “either thus or thus,” it is as though a questioner asked: what is the first and what is the second? So he said: “the second is the particle,” and “the first is either thus or thus,” conjoined to the resumptive sentence."},
    {"type": "pair",
     "ar": "ولك أن تعطف أولا ثم تجعل المجموع جوابا. وكذا الحال في قوله: الثاني الاسم، والأول الفعل.",
     "en": "You may [instead] conjoin first and then make the whole [into] the answer. The same holds in his statement: “the second is the noun,” and “the first is the verb.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن تفسير معنى «من» و«إلى» بالابتداء والانتهاء غير صحيح، فإن معنى هذين اللفظين معنى مستقل بالمفهومية، فلا يكون معنى «من» و«إلى»؛",
     "en": "In it [is a difficulty]: that explaining the meaning of “min” and “ilā” by “origination” and “termination” is incorrect, for the meaning of these two words is a meaning independent in conceptuality, so it cannot be the meaning of “min” and “ilā”;"},
    {"type": "pair",
     "ar": "ولأنه لو كان معنى الابتداء والانتهاء معنى «من» و«إلى» يكون معناهما معنى حرفيا، فيكون لفظ الابتداء والانتهاء حرفين، ولأنه مخالف لما سيأتي من أنهما موضوعان لجزئيات معنى الابتداء والانتهاء.",
     "en": "and because, were “origination” and “termination” the meaning of “min” and “ilā,” their meaning would be a particle-meaning (ḥarfī), so the words “ibtidāʾ” and “intihāʾ” would themselves be two particles; and because it contradicts what will come — that the two are coined for the particular instances of the meaning of origination and termination."},
    {"type": "pair",
     "ar": "والجواب: أن المراد من الابتداء والانتهاء هو جزئياتهما بتقدير المضاف، فتأمل.",
     "en": "The answer: what is intended by “origination” and “termination” is their particular instances, by estimating an omitted governing noun (bi-taqdīr al-muḍāf); so reflect (fa-taʾammal)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يفهم من ظاهر هذه العبارة أن احتياج كلمة «من» و«إلى» في الدلالة على معناهما إلى مدخولهما فقط، مع أن الواقع ليس كذلك، فإن معناهما نسبتان مخصوصتان بين متعلقهما ومدخولهما،",
     "en": "From the outward of this expression it is understood that the need of the words “min” and “ilā,” in signifying their meaning, is for their object of entry (madkhūl) alone — whereas the reality is not so, for their meaning is two specific relations between their governed term (mutaʿallaq) and their object of entry;"},
    {"type": "pair",
     "ar": "فلا بد من ذكر متعلقهما أيضا، إلا أن يقال: مقصوده التنبيه على احتياج الحروف في الدلالة على معناه إلى ضميمة، فاكتفى بذكر بعض الضميمات. ويمكن جعل قوله: «كالبصرة» إشارة إلى ذلك أيضا.",
     "en": "so mentioning their governed term is likewise indispensable — unless it be said: his aim is to alert [us] to the need of particles, in signifying their meaning, for an adjunct (ḍamīma), so he confined himself to mentioning some of the adjuncts. It is possible to take his statement “such as al-Baṣra” as pointing to this as well."},
]
