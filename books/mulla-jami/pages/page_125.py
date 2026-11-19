# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 125 (printed ١٢٤)."""

PAGE_NUMBER = 125
PRINTED_PAGE = "١٢٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "فأجاب عنه المصنف بقوله: (ولا يلزمه) أي: سيبويه من اعتبار الوصفية الأصلية بعد التنكير في مثل: «أحمر» علما (باب حاتم) أي: كل علم كان في الأصل وصفا مع بقاء العلمية، بأن اعتبر فيه أيضا الوصفية الأصلية، وحكم بمنع صرفه للعلمية والوصفية الأصلية",
     "en": "The author answered it with his words “and it does not follow for him” (wa-lā yalzamuhu) — that is, [it does not follow] for Sībawayh, from taking into account the original adjectival status (waṣfiyya aṣliyya) after indefiniteness in a case such as “aḥmar” [used] as a proper name — “the category of Ḥātim” (bāb Ḥātim): that is, every proper name that was originally an adjective while the proper-name status remains, in that the original adjectival status is also taken into account in it, and he ruled that it be barred from full inflection (ṣarf) on account of the proper-name status and the original adjectival status."},
    {"type": "matn",
     "ar": "(لما يلزم) في «باب حاتم» على تقدير منعه من الصرف (من اعتبار المتضادين) يعني: الوصفية والعلمية، فإن العلم للخصوص[[١]]، والوصف للعموم (في حكم واحد)[[٢]] وهو منع صرف لفظ واحد،",
     "en": "“Because of what would follow” (li-mā yalzamu) — in “the category of Ḥātim,” on the assumption of its being barred from full inflection — “from taking into account the two contraries” (min iʿtibār al-mutaḍāddayn), meaning: the adjectival status and the proper-name status; for the proper name is for the particular, while the adjective is for the general, “within a single ruling” (fī ḥukmin wāḥid), which is the barring of a single word from full inflection."},
    {"type": "matn",
     "ar": "بخلاف ما إذا اعتبرت الوصفية الأصلية مع سبب آخر، كما في «أسود» و«أرقم».",
     "en": "This is unlike the case in which the original adjectival status is taken into account together with another cause, as in “aswad” (black) and “arqam” (a kind of speckled snake)."},
    {"type": "matn",
     "ar": "فإن قلت: التضاد إنما هو بين الوصفية المحققة[[٣]] والعلمية[[٤]]، لا بين الوصفية الأصلية الزائلة والعلمية، فلو اعتبرت الوصفية الأصلية والعلمية في منع صرف مثل: «حاتم» لا يلزم اجتماع المتضادين؟",
     "en": "If you say: contrariety obtains only between actualized adjectival status and proper-name status, not between the original, now-departed adjectival status and the proper-name status; so if the original adjectival status and the proper-name status were taken into account in barring the full inflection of a case such as “Ḥātim,” the conjunction of the two contraries would not follow?"},
    {"type": "matn",
     "ar": "قلنا: تقدير أحد الضدين بعد زواله مع ضد آخر في حكم واحد، وإن لم يكن من قبيل اجتماع المتضادين، لكنه شبيه به، فاعتبارهما معا غير مستحسن[[٥]].",
     "en": "We say: the positing of one of the two contraries, after its departure, together with another contrary within a single ruling — though it is not of the type of the conjunction of two contraries — is nonetheless similar to it, so taking both of them into account together is not commendable."},

    {"type": "section", "ar": "[ انكسار غير المنصرف ]",
     "en": "The Kasra-Inflection of the Diptote"},

    {"type": "matn",
     "ar": "(وجميع الباب) أي: باب غير المنصرف[[٦]]:",
     "en": "“And the whole category” (wa-jamīʿ al-bāb) — that is, the category of the diptote (ghayr al-munṣarif):"},
    {"type": "matn",
     "ar": "١-(باللام) أي: بدخول لام التعريف عليه، ٢-(أو الإضافة) أي: إضافته إلى غيره.",
     "en": "1- “with the lām” (bi-l-lām) — that is, by the definite article’s being prefixed to it; 2- “or the genitive construction” (aw al-iḍāfa) — that is, its being annexed to something else."},
    {"type": "matn",
     "ar": "(ينجر) أي: يصير مجرورا (بالكسر) أي: بصورة الكسر[[٧]] لفظا أو تقديرا.",
     "en": "“Becomes drawn into the genitive” (yanjarru) — that is, it becomes governed in the genitive — “with the kasra” (bi-l-kasr) — that is, with the form of the kasra, whether in pronunciation or in estimation (taqdīr)."},
    {"type": "matn",
     "ar": "وإنما لم يكتف بقوله: «ينجر»؛ لأن الانجرار قد يكون بالفتح، ولا بأن يقول: «ينكسر»؛ لأن الكسر يطلق على الحركات البنائية أيضا.",
     "en": "He did not content himself with saying “it becomes drawn into the genitive” only, because being drawn into the genitive may [also] occur with the fatḥa; nor [did he content himself] with saying “it takes a kasra” (yankasir), because “kasr” is applied to the vowels of indeclinability (al-ḥarakāt al-bināʾiyya) as well."},
    {"type": "matn",
     "ar": "وللنحاة خلاف في أن هذا",
     "en": "The grammarians hold a disagreement as to whether this [noun…]"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: موضوع للخاص، والوصف مذكور للعام، والأوضح في بيان التضاد، فإن العلمية كون اللفظ موضوعا لذات معينة من غير اعتبار صفة، والوصفية كونها مستعملة في ذات مبهمة في غاية الإبهام مع اعتبار صفة.",
     "en": "That is: [the proper name] is coined for the particular, and the adjective is mentioned for the general; and the clearer [way of putting it], in explaining the contrariety, is that proper-name status is the word’s being coined for a determinate entity without regard to an attribute, whereas adjectival status is its being used for an utterly indeterminate entity together with regard to an attribute."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في شأن أثر واحد وتحصيله.",
     "en": "That is: with respect to a single effect and its production."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بالفعل لا المفروضة.",
     "en": "That is: the [adjectival status] actualized in fact, not the hypothetically posited one."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الحالية.",
     "en": "That is: the presently obtaining [proper-name status]."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يخفى عليك أن سوق الدليل قبل إيراد السؤال بقوله: «فإن قلت»، وجوابه أن اللازم أي: اعتبار متضادين في حكم واحد باطل، ويقتضي جوابه أن اعتبار الوصفية حال العلمية غير مستحسن.",
     "en": "It is not hidden from you that the proof was adduced before the raising of the question with his words “if you say,” and its answer is that the necessary consequence — namely, taking two contraries into account within a single ruling — is void; and his answer entails that taking the adjectival status into account concurrently with the proper-name status is not commendable."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن اللام للعهد.",
     "en": "He means: that the lām [in “the whole category”] is for definite reference (ʿahd)."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: أنه أراد بالكسر صورة الكسر بطريق الاستعارة؛ لأن الكسر بلا تاء من ألقاب البناء عند البصريين. ويطلق على الحالة الإعرابية مجازا.",
     "en": "He means: by “kasr” he intended the form of the kasra by way of metaphor; for “kasr” — without the tāʾ [i.e., not “kasra”] — is among the technical designations of indeclinability (bināʾ) according to the Baṣrans, and it is applied to the inflectional state (al-ḥāla al-iʿrābiyya) [only] figuratively."},
    {"type": "pair",
     "ar": "فالظاهر أن يقول بالكسرة لعدم اختصاصها بالبناء.",
     "en": "So what would have been apparent is that he should say “with the kasra” (bi-l-kasra), since it [i.e., “kasra” with the tāʾ] is not restricted to indeclinability."},
]
