# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 241 (printed ٢٤٠)."""

PAGE_NUMBER = 241
PRINTED_PAGE = "٢٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «إذ لم يمكن حمله على الزمان المبهم» from the foot of PDF p. 240.
    {"type": "matn",
     "ar": "لاختلافهما ذاتا وصفة، نحو: «جلست في المسجد».",
     "en": "…because they differ in essence and in attribute; as in “I sat in the mosque.”"},
    {"type": "matn",
     "ar": "(وفسر المبهم) من المكان (بالجهات الست[[١]]) وهي: «أمام، وخلف، ويمين، وشمال، وفوق، وتحت»، وما في معناها،",
     "en": "(The indefinite) of place (has been explained as the six directions): “in front, behind, right, left, above, below,” and what has their meaning;"},
    {"type": "matn",
     "ar": "فإن «أمام زيد» مثلا يتناول جميع ما يقابل وجهه إلى انقطاع الأرض، فيكون مبهما.",
     "en": "for “in front of Zayd,” for example, covers everything facing his face up to where the earth ends, and so it is indefinite."},
    {"type": "matn",
     "ar": "ولما لم يتناول هذا التفسير بعض الظروف المكانية الجائز نصبها قال (وحمل عليه) أي: على المبهم المفسر بالجهات الست («عند[[٢]] ولدى» وشبههما) نحو: «دون وسوى»",
     "en": "Since this explanation does not cover some adverbs of place whose accusative is allowed, he said: (And assimilated to it)—that is, to the indefinite explained as the six directions—(are “ʿinda” and “ladā” and what resembles them), such as “dūna” and “siwā,”"},
    {"type": "matn",
     "ar": "(لإبهامهما[[٣]]) أي: لإبهام «عند ولدى»، ولم يذكر وجه حمل شبههما عليه؛ لأن حكمه حكمهما.",
     "en": "(because of their indefiniteness), that is, the indefiniteness of “ʿinda” and “ladā.” He did not mention the reason for assimilating what resembles them to it, because its rule is their rule."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «لإبهامها» كما هو الظاهر.",
     "en": "In some copies: “li-ibhāmihā” (because of their indefiniteness, plural), as is apparent."},
    {"type": "matn",
     "ar": "وكذا حمل على المبهم من المكان (لفظ «مكان»[[٤]]) وإن كان معينا، نحو: «جلست مكانك» (لكثرته) في الاستعمال مثل الجهات الست لا لإبهامه.",
     "en": "Likewise assimilated to the indefinite of place is (the word “makān” [place]), even if it is specific, as in “I sat in your place” (because of its frequency) in use, like the six directions, not because of its indefiniteness."},
    {"type": "matn",
     "ar": "(و) كذا حمل عليه (ما بعد «دخلت»[[٥]]) وإن كان معينا (نحو: «دخلت الدار»)",
     "en": "(And) likewise assimilated to it is (what comes after “dakhaltu” [I entered]), even if it is specific, (as in “I entered the house”)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا تفسير أكثر المتقدمين. وأما تفسير غيرهم، فمنهم من قال: إن المبهم من المكان هو النكرة، والمعين منه هو المعرفة.",
     "en": "This is the explanation of most of the earlier [grammarians]. As for others’ explanation: some of them said the indefinite of place is the indeterminate noun (nakira), and the specific of it is the determinate (maʿrifa)."},
    {"type": "pair",
     "ar": "وفيه أن نحو خلفك معرفة مع أنه منصوب اتفاقا.",
     "en": "Against this is that something like “khalfaka” (behind you) is determinate, although it is in the accusative by agreement."},
    {"type": "pair",
     "ar": "ويمكن دفعه بأنه ملحق بالنكرة لإبهامه أو بأنه نكرة حقيقة لما قاله الفاضل الهندي في الإرشاد من أن الجهات الست لا تتعرف بالإضافة كما لا يتعرف مثل بها.",
     "en": "This may be answered: it is attached to the indeterminate because of its indefiniteness; or it is truly indeterminate, given what al-Fāḍil al-Hindī said in al-Irshād, that the six directions do not become determinate by annexation, just as “mithl” does not become determinate by it."},
    {"type": "pair",
     "ar": "ومنهم من فسرهما بمثل ما فسر المبهم والمعين من الزمان،",
     "en": "Some of them explained the two in the same way as the indefinite and the specific of time were explained;"},
    {"type": "pair",
     "ar": "وتدخل في المبهم الجهات الست، وعند، ولدى ووسط وبين وتلقاء، وليس كل منهم عندهم جائز النصب؛",
     "en": "under the indefinite then fall the six directions, “ʿinda,” “ladā,” “wasṭ,” “bayna” and “tilqāʾ”; yet not every one of them, in their view, admits the accusative;"},
    # REVIEW: print reads «وذري» (probably «ذرى»); transcribed as printed.
    {"type": "pair",
     "ar": "لأن جانب وما بمعناه من جهة ووجه بمعناها، وكنف وذري لا يقال فيها مثلا زيد جانب عمرو بل يقال: في جانبه أو إلى جانبه. وكذا خارج وداخل",
     "en": "for of “jānib” (side) and what has its meaning—“jiha” and “wajh” in its sense, and “kanaf” and “dharī”—one does not say, for example, “Zayd is jāniba ʿAmr,” but rather “fī jānibihi” or “ilā jānibihi”; and likewise “khārij” and “dākhil.”"},
    # REVIEW: print reads «وليس أيضا كان معين»; probably «كل معين»; transcribed as printed.
    {"type": "pair",
     "ar": "وليس أيضا كان معين مجرورا عندهم، فإن المقادير المسموحة كالفرسخ، والميل منصوبة.",
     "en": "Nor, again, is every specific [place] in the genitive in their view; for measured distances, such as the parasang (farsakh) and the mile (mīl), are in the accusative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ينبغي أن يذكر أمر المقادير المسموحة أيضا، فإنها منصوبة اتفاقا.",
     "en": "He ought to have mentioned the matter of measured distances too, for they are in the accusative by agreement."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ينبغي أن تحمل على الجهات الست لمشابهتها لها في الانتقال،",
     "en": "Shaykh al-Raḍī said: they should be assimilated to the six directions, because they resemble them in shifting;"},
    {"type": "pair",
     "ar": "فإن تعيين ابتداء الفرسخ مثلا لا يختص موضعا دون موضع، بل يتحول ابتداؤه وانتهاؤه كتحول الخلف قداما واليمين شمالا.",
     "en": "for the fixing of a parasang’s starting point, for example, is not confined to one spot rather than another; rather its start and end shift, just as “behind” turns into “in front” and “right” into “left.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أراد بالإبهام اللغوي لا ما يشتق منه المبهم الاصطلاحي.",
     "en": "He meant indefiniteness in the lexical sense, not that from which the technical “mubham” is derived."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بشرط أن يكون في عامله معنى الاستقرار، فلا يقال: كتبت المصحف مكان كذا.",
     "en": "On condition that its governor has the sense of settling (istiqrār); so one does not say “I wrote the muṣḥaf in such-and-such a place (makāna kadhā).”"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: اسم المكان الذي في أوله ميم زائدة إن كان مشتقا من حدث بمعنى الاستقرار، والكون ينتصب بالدال على ذلك الحدث،",
     "en": "Shaykh al-Raḍī said: a noun of place beginning with an augment mīm, if it is derived from an event in the sense of settling and being, takes the accusative by what signifies that event,"},
    {"type": "pair",
     "ar": "وبما ينتصب به المكان المختص وهو \"دخلت وسكنت ونزلت\" وإن لم يكن كذلك، فلا ينتصب إلا بما ينتصب به المكان المختص.",
     "en": "and by what puts the specific place in the accusative, namely “dakhaltu,” “sakantu” and “nazaltu” (I entered, dwelt, alighted); if it is not so, it takes the accusative only by what puts the specific place in the accusative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وكذا سكنت ونزلت.",
     "en": "And likewise “sakantu” and “nazaltu.”"},
]
