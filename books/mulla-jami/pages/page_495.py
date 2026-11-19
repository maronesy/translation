# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 495 (printed ٤٩٤)."""

PAGE_NUMBER = 495
PRINTED_PAGE = "٤٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فعلى هذا قوله: «أيهم سار» عطف على «كان» at the foot of PDF p. 494.
    {"type": "matn",
     "ar": "سيري» ولا فساد فيه.",
     "en": "…sayrī”, and there is nothing wrong in that."},
    {"type": "matn",
     "ar": "(و«لام» كي) التي ينتصب المضارع بعدها بتقدير: «أن» (مثل: «أسلمت لأدخل الجنة») وإنما يقدر «أن» بعدها؛ لأنها جارة.",
     "en": "(And the “lām” of kay), after which the muḍāriʿ is put in the accusative by supposing “an”, (as in “aslamtu li-adkhula al-jannata” (I embraced Islam in order to enter Paradise)). “An” is supposed after it only because it governs the genitive."},
    {"type": "matn",
     "ar": "(و«لام» الجحود) التي ينتصب بها المضارع (هي لام تأكيد[[١]]) للنفي (بعد النفي لـ«كان») لفظا (مثل: ﴿وما كان الله ليعذبهم﴾[[٢]]) أو معنى نحو: «لم يكن ليفعل»،",
     "en": "(And the “lām” of denial (lām al-juḥūd)), by which the muḍāriʿ is put in the accusative, (is a lām of corroboration) of the negation, (after the negation of “kāna”), in wording, (as in “But Allah would not punish them” (wa-mā kāna Allāhu li-yuʿadhdhibahum)), or in meaning, as in “lam yakun li-yafʿala” (he was not one to do [it]);"},
    {"type": "matn",
     "ar": "وهي أيضا جارة؛ ولهذا يقدر بعدها «أن».",
     "en": "it too governs the genitive, and for this reason “an” is supposed after it."},
    {"type": "matn",
     "ar": "فإن قيل[[٣]]: إذا صار الفعل بمعنى المصدر بـ«أن» المقدرة فكيف يصح الحمل؟",
     "en": "If it is said: when the verb takes on the sense of a verbal noun (maṣdar) through the supposed “an”, how can the predication be sound?"},
    {"type": "matn",
     "ar": "قيل: على حذف المضاف من الاسم أي: ما كان صفة الله تعذيبهم، أو من الخبر أي: ما كان الله ذا تعذيبهم، أو على تأويل المصدر باسم الفاعل أي: ما كان الله معذبهم.",
     "en": "It is said: [it is] by omission of the first term of a genitive construction from the subject [of kāna], that is, “Allah’s attribute was not their punishment”; or from the predicate, that is, “Allah was not one possessing their punishment”; or by interpreting the verbal noun as an active participle, that is, “Allah was not their punisher.”"},
    {"type": "matn",
     "ar": "(والفاء) التي ينتصب المضارع بعدها بتقدير «أن»، فتقدير «أن» بعدها لانتصاب المضارع مشروط (بشرطين):",
     "en": "(And the fāʾ), after which the muḍāriʿ is put in the accusative by supposing “an”; supposing “an” after it, so that the muḍāriʿ is in the accusative, is conditional (on two conditions):"},
    {"type": "matn",
     "ar": "(أحدهما: السببية) أي: سببية ما قبلها لما بعدها؛ لأن العدول عن الرفع إلى النصب للتنصيص على السببية[[٤]] حيث يدل تغيير اللفظ[[٥]] على تغيير المعنى،",
     "en": "(The first of them is causation), that is, the causation by what precedes it of what follows it; because turning from the nominative to the accusative serves to state the causation explicitly, in that the change of wording indicates a change of meaning;"},
    {"type": "matn",
     "ar": "فإذا لم يقصد السببية لا يحتاج إلى الدلالة عليها.",
     "en": "so when causation is not intended, there is no need to indicate it."},
    {"type": "matn",
     "ar": "(والثاني: أن يكون قبلها) أي: قبل الفاء، أحد الأشياء الستة: ليبعد بتقديم الإنشاء[[٦]] أو ما في معناه من النفي المستدعي جوابا[[٧]] عن توهم[[٨]] كون ما بعدها جملة معطوفة",
     "en": "(The second is that there be before it), that is, before the fāʾ, one of the six things; so that, by placing first an injunctive utterance (inshāʾ), or a negation in its sense that calls for an answer, [the sentence] is kept far from the illusion that what follows it is a coordinated sentence…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خبر مبتدأ محذوف، والجملة معترضة بين المبتدأ والخبر.",
     "en": "The predicate of an omitted subject; and the sentence is parenthetical between the subject and the predicate."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأنفال:٣٣.",
     "en": "(Qurʾān, Sūrat al-Anfāl 8:33)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا ورود لهذا السؤال؛ لأن اللام عند الكوفيين زائدة لمجرد تأكيد النفي، وعند البصريين صلة لخبر محذوف أعني: قاصدا.",
     "en": "This question does not arise; for according to the Kufans the lām is redundant, serving merely to corroborate the negation, and according to the Basrans it is attached to an omitted predicate, namely “intending” (qāṣidan)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: كون الفاء سببية لا عاطفة للجملة على الجملة، فلا ينافي كونها لعطف المفرد على المفرد.",
     "en": "That is, the fāʾ’s being causal, not coordinating a sentence upon a sentence; so this is not incompatible with its coordinating a single term upon a single term."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "من الرفع الذي هو الأصل في جميع الأفعال الخالية من النواصب والجوازم إلى النصب لا تغيير اللفظ في نفسه،",
     "en": "[That is, its change] from the nominative, which is the default in all verbs free of accusative and jussive governors, to the accusative; not a change of the word in itself,"},
    {"type": "pair",
     "ar": "حتى يرد أن تغيير الإعراب لا يقال له تغيير اللفظ.",
     "en": "so that the objection might be raised that a change of inflection (iʿrāb) is not called a change of wording."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأن تقديم الإنشاء على ما يصح أن يكون جوابا يدل على أنه خال عن الطلب الذي هو مدلول الإنشاء، فيكون جوابا، والجواب لا يعطف.",
     "en": "Because placing the injunctive utterance before what can properly be an answer indicates that it [what follows] is free of the request that the injunctive utterance signifies, so it is an answer; and an answer is not coordinated."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "صفة للنفي مبينة لكونه في معنى الإنشاء.",
     "en": "A description of the negation, making clear that it is in the sense of an injunctive utterance."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إنما قال: توهم لأن دفع احتمال عطف الجملة على الجملة حصل بنصب المضارع إلا أن توهمه باق باعتبار غفلة السامع عن النصب.",
     "en": "He said “illusion” only because the possibility of coordinating a sentence upon a sentence is already removed by the accusative of the muḍāriʿ; but the illusion of it remains, in view of the hearer’s inattention to the accusative."},
]
