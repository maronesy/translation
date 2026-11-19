# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 340 (printed ٣٣٩)."""

PAGE_NUMBER = 340
PRINTED_PAGE = "٣٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «إذ «بين» لا يضاف إلا إلى المتعدد.» at the foot of PDF p. 339 (new sentence).
    {"type": "matn",
     "ar": "وقيل: جره بالثاني كما في الحرف[[١]] الزائد في «كفى بالله»،",
     "en": "It has been said: its genitive is by the second, as with the redundant particle in “kafā bi-llāh” (Allah suffices)."},
    {"type": "matn",
     "ar": "وهذا الذي ذكرناه أعني: لزوم إعادة الجار في حال السعة والاختيار مذهب البصريين، ويجوز عندهم تركها اضطرارا،",
     "en": "What we have stated, I mean the necessity of repeating the preposition in free and unconstrained usage, is the doctrine of the Baṣrans; with them its omission is permitted under [metrical] necessity (iḍṭirāran);"},
    {"type": "matn",
     "ar": "وأجاز الكوفيون ترك الإعادة في حال السعة مستدلين بالأشعار[[٢]].",
     "en": "while the Kūfans permitted omitting the repetition in free usage, adducing verses of poetry as evidence."},
    {"type": "matn",
     "ar": "فإن قيل: كيف جاز تأكيد المرفوع المتصل في نحو: «القوم جاؤوني كلهم»[[٣]]، والإبدال منه نحو: «أعجبني جمالك» من غير شرط تقدم التأكيد بالمنفصل،",
     "en": "If it is said: how is it permitted to corroborate the attached nominative [pronoun], as in “al-qawmu jāʾūnī kulluhum” (the people, they all came to me), and to substitute for it, as in “aʿjabanī jamāluki” (your beauty pleased me), without the condition of a prior corroboration by a detached [pronoun];"},
    {"type": "matn",
     "ar": "وجاز أيضا تأكيد الضمير المجرور في نحو: «مررت بك نفسك»، والإبدال منه نحو: «أعجبت بك جمالك» من غير إعادة الجار،",
     "en": "and likewise permitted to corroborate the genitive pronoun, as in “marartu bika nafsika” (I passed by you yourself), and to substitute for it, as in “aʿjabtu bika jamālika” (I admired you, your beauty), without repeating the preposition;"},
    {"type": "matn",
     "ar": "ولم يجز العطف في الأول إلا بعد التأكيد بالمنفصل، وفي الثاني إلا مع إعادة الجار؟",
     "en": "while conjunction is not permitted in the first case except after corroboration by a detached [pronoun], nor in the second except with repetition of the preposition?"},
    {"type": "matn",
     "ar": "قلنا: التأكيد عين المؤكد، والبدل في الأغلب إما كل المتبوع أو بعضه أو متعلقه، والغلط قليل نادر،",
     "en": "We say: the corroborative is identical with the corroborated; and the substitute is mostly either the whole of the followed noun, or part of it, or something connected with it, while [the substitute of] error is uncommon and rare;"},
    {"type": "matn",
     "ar": "فهما ليسا بأجنبيين لمتبوعهما ولا منفصلين عنه، لعدم تخلل فاصل بينهما وبين متبوعهما، فلا حاجة في ربطهما إلى متبوعهما إلى تحصيل مناسبة زائدة،",
     "en": "so the two are neither foreign to the noun they follow nor separate from it, since no separator intervenes between them and it; and there is no need, in tying them to it, to secure any additional affinity."},
    {"type": "matn",
     "ar": "بخلاف العطف، فإن المعطوف يغاير المعطوف عليه، ويتخلل بينهما العاطف،",
     "en": "Conjunction is otherwise, for the conjoined noun differs from the noun conjoined to, and the conjunctive particle intervenes between them;"},
    {"type": "matn",
     "ar": "فلا بد فيه من تحصيل مناسبة بينهما بتأكيد المتصل بالمنفصل في المرفوع، وبإعادة الجار في المجرور",
     "en": "so in it an affinity between them must be secured: by corroborating the attached by the detached [pronoun] in the nominative, and by repeating the preposition in the genitive,"},
    {"type": "matn",
     "ar": "ليخرج المتصل المرفوع عن صرافة الاتصال، ويناسب المعطوف عليه بتأكيده بالمنفصل، وقوي[[٤]] مناسبة المجرور بانضمام الجار إليه كما في المعطوف عليه.",
     "en": "so that the attached nominative leaves pure attachment and the noun conjoined to gains affinity through its corroboration by the detached [pronoun]; and the affinity of the genitive grows stronger by the preposition’s being joined to it, as in the noun conjoined to."},
    {"type": "matn",
     "ar": "(والمعطوف في حكم المعطوف عليه) فيما يجوز له، ويمتنع من الأحوال العارضة له نظرا إلى ما قبله بشرط ألا يكون ما يقتضيها منتفيا في المعطوف.",
     "en": "(The conjoined noun has the status of the noun conjoined to) in what is permitted to it and what is barred among the states that befall it with regard to what precedes it, provided that what requires them is not absent in the conjoined noun."},
    {"type": "matn",
     "ar": "وإنما قلنا: «من الأحوال العارضة له» نظرا إلى ما قبله احترازا عن الأحوال العارضة له من حيث نفسه كالإعراب[[٥]] والبناء والتعريف والتنكير والإفراد والتثنية والجمع،",
     "en": "We said “among the states that befall it with regard to what precedes it” only to exclude the states that befall it in respect of itself, such as inflection (iʿrāb), indeclinability (bināʾ), definiteness, indefiniteness, singular, dual and plural;"},
    {"type": "matn",
     "ar": "فإن المعطوف",
     "en": "for the conjoined noun…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أنه ليس بأقل من الحروف الزائدة.",
     "en": "He means: it is not less than the redundant particles."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه إشعار بضعف استدلالهم، لكن لا يقتصر استدلالهم على الأشعار، بل استدلوا بالقرآن العظيم أيضا،",
     "en": "This hints at the weakness of their argument; yet their argument is not confined to poetry, for they also adduced the Mighty Qurʾān,"},
    {"type": "pair",
     "ar": "وهو قوله تعالى: ﴿تساءلون به والأرحام﴾ (سورة النساء: ١) وأجيب: بجعل قوله: والأرحام قسما.",
     "en": "namely His words, Exalted is He, “through whom you ask one another, and the wombs” (Qurʾān, Sūrat al-Nisāʾ 4:1). It has been answered by taking His words “wa-l-arḥām” as an oath."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: the note prints «أعجبتني جمالك» and «عجبت جمالك زيدا», whereas the matn has «أعجبني جمالك»; transcribed as printed.
    {"type": "pair",
     "ar": "فيه أنه لا إشكال في جواز جاؤوني كلهم، وجواز أعجبتني جمالك لوجود الفصل،",
     "en": "Against this: there is no difficulty in the permissibility of “jāʾūnī kulluhum” and of “aʿjabatnī jamāluki”, because a separation is present;"},
    {"type": "pair",
     "ar": "فالأولى التمثيل بـ«جاؤوا كلهم زيدا» و«عجبت جمالك زيدا».",
     "en": "so it would be better to exemplify by “jāʾū kulluhum Zaydan” and “ʿajabat jamāluki Zaydan”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر: وليقوى؛ إذ هو معطوف على «ليخرج».",
     "en": "The evident [reading] is “wa-li-yaqwā” (and so that it grows stronger), since it is conjoined to “li-yakhruja” (so that it leaves)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الإعراب من الأحوال العارضة نظرا إلى العامل.",
     "en": "Inflection is among the states that befall [a noun] with regard to the governor (ʿāmil)."},
    {"type": "pair",
     # REVIEW: «نعم قابليته الإعراب كذلك» is clearly printed but terse (perhaps «قابليته للإعراب»).
     "ar": "وأما خصوص من الإعراب من كونه بالحركة أو الحروف فهو من الأحوال العارضة له بالنظر إلى نفسه تأمل؛ لأن للعامل دخلا فيه، نعم قابليته الإعراب كذلك.",
     "en": "As for the particular [kind] of inflection, its being by a vowel or by letters, it is among the states that befall it in respect of itself; reflect, for the governor has a share in it. Yes, its capacity for inflection is so."},
]
