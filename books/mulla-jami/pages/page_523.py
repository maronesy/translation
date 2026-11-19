# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 523 (printed ٥٢٢)."""

PAGE_NUMBER = 523
PRINTED_PAGE = "٥٢٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وراح»، فأسقطها عن» at the foot of PDF p. 522 (mid-sentence).
    {"type": "matn",
     "ar": "البين إشارة إلى عدم الاعتداد بها[[١]]؛ لأنها من الملحقات.",
     "en": "…the discussion, as an indication that they are not taken into account, because they are among the appended verbs."},
    {"type": "matn",
     "ar": "(و«ما زال») من «زال يزال» لا من «زال يزول» فإنها تامة.",
     "en": "(And “mā zāla”), from “zāla yazālu”, not from “zāla yazūlu”, for the latter is complete."},
    {"type": "matn",
     "ar": "(و«ما برح») بمعناه من «برح» أي: زال، ومنه: «البارحة لليلة الماضية»[[٢]].",
     "en": "(And “mā bariḥa”), in its sense, from “bariḥa”, that is, “zāla” (to depart); from it comes “al-bāriḥa” for the past night."},
    {"type": "matn",
     "ar": "(و«ما فتئ») أيضا بمعناه (و«ما انفك») أي: ما انفصل (لاستمرار خبرها) أي: خبر تلك الأفعال (لفاعلها)",
     "en": "(And “mā fatiʾa”), also in its sense, (and “mā infakka”), that is, “it did not separate”, (are for the continuance of their predicate), that is, the predicate of those verbs, (for their agent [fāʿil]);"},
    {"type": "matn",
     "ar": "قيل: سمي اسمها فاعلا[[٣]] تنبيها على أن اسمها ليس بقسم على حدة من المرفوعات، كما أن خبرها قسم على حدة من المنصوبات",
     "en": "it has been said: their noun was called the agent in order to point out that their noun is not a separate category among the nominatives, just as their predicate is a separate category among the accusatives."},
    {"type": "matn",
     "ar": "(مذ قبله) أي: قبل فاعلها خبرها أي: من وقت يمكن أن يقبله عادة،",
     "en": "(Ever since it admitted it), that is, since their agent admitted their predicate, that is, from the time when it could customarily admit it;"},
    {"type": "matn",
     "ar": "فمعنى «ما زال زيد أميرا» استمرار إمارته من زمان قابليته وصلاحيته للإمارة.",
     "en": "so the meaning of “mā zāla Zaydun amīran” (Zayd has continued to be a ruler) is the continuance of his rule from the time of his capacity and fitness for rule."},
    # REVIEW: printed «إما دلالتها» where the sense calls for «أما»; transcribed as printed.
    {"type": "matn",
     "ar": "إما دلالتها على الاستمرار، فلأن النفي مأخوذ في معاني هذه الأفعال، فإذا دخلت أدوات النفي عليها كانت معانيها نفي النفي،",
     "en": "As for their indicating continuance, it is because negation is included in the meanings of these verbs; so when the particles of negation enter upon them, their meanings become the negation of a negation;"},
    {"type": "matn",
     "ar": "ونفي النفي استمرار الثبوت واعتبار الصلاحية والقابلية معلوم عقلا",
     "en": "and the negation of a negation is the continuance of affirmation; and the consideration of fitness and capacity is known rationally."},
    {"type": "matn",
     "ar": "(ويلزمها) أي: هذه الأفعال الأربعة إذا أريد بها استمرار الثبوت (النفي) بدخول أدواته عليها لفظا، وهو ظاهر، أو تقديرا[[٤]]",
     "en": "(And they necessarily take), that is, these four verbs, when continuance of affirmation is meant by them, (negation), through its particles entering upon them, either explicitly, which is obvious, or by supposition,"},
    {"type": "matn",
     "ar": "كقوله تعالى[[٥]]: ﴿تالله تفتأ تذكر يوسف﴾[[٦]] أي: لا تفتؤ،",
     "en": "as in His words, the Exalted: “By Allah, you will not cease remembering Joseph”, that is, “lā taftaʾu”;"},
    {"type": "matn",
     "ar": "فإنه لو لم تدخل أدوات النفي عليها لم يلزم نفي النفي المستلزم للاستمرار المقصود منها.",
     "en": "for if the particles of negation did not enter upon them, there would not result the negation of a negation that entails the continuance intended by them."},
    {"type": "matn",
     "ar": "(و«ما دام»: لتوقيت أمر) أي: تعيينه (بمدة ثبوت خبرها لفاعلها) بأن جعلت تلك المدة ظرف زمان له،",
     "en": "(And “mā dāma” is for timing a matter), that is, fixing it, (by the duration of the predicate’s holding for its agent), in that this duration is made a temporal adverbial for it;"},
    {"type": "matn",
     "ar": "وذلك لأن لفظة «ما» مصدرية، فهي مع ما بعدها في تأويل المصدر، وتقدير الزمان قبل المصادر كثير، وإذا قدر الزمان قبله فلا بد هناك من",
     "en": "that is because the word “mā” is maṣdariyya (verbal-noun forming), so together with what follows it it is construed as a maṣdar; supplying [a word for] time before verbal nouns is frequent; and when time is supplied before it, there must then be…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فالذكر في الإجمال لكونها ناقصة في الجملة، وعدم الذكر في التفصيل إشارة إلى عدم الاعتداد.",
     "en": "So the mention in the summary is because they are incomplete in general, and the non-mention in the detailed exposition is an indication that they are not taken into account."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بلا فصل على ما في القاموس: البارحة أقرب ليلة مضت.",
     "en": "Without interval, according to what is in al-Qāmūs: “al-bāriḥa is the nearest night that has passed.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قد فات هذا القائل هذا التنبيه في محله، وهو قوله: ما وضع لتقرير الفاعل على صفة.",
     "en": "This speaker missed that this pointing-out is in its proper place, namely his [the author’s] words “what was coined to establish the agent in an attribute”."},
    {"type": "pair",
     "ar": "ولا يخفى أن هذا التنبيه ليس في مرتبة لاختصاص الإطلاق ببعض الأفعال.",
     "en": "It is not hidden that this pointing-out is not on a par [with it], because the usage is restricted to some of the verbs."},
    {"type": "pair",
     "ar": "ونحن نقول: نبه في هذا الكلام بجميع الخبر مع الفاعل على أن الاصطلاح على التسمية بالفاعل بجامع الاصطلاح على التسمية بالخبر،",
     "en": "We say: by combining “the predicate” with “the agent” in this statement he pointed out that the convention of calling it the agent goes together with the convention of calling [the other] the predicate,"},
    # REVIEW: printed «بجميع الخبر مع الفاعل»; «بجمع» may be intended. Transcribed as printed.
    {"type": "pair",
     "ar": "وليس الخبر على اصطلاح ما يسمى الاسم فيه فاعلا مسمى باسم المفعول، بل الاسم يسمى فاعلا واسما كما أنه يسمى الخبر مفعولا وخبرا.",
     "en": "and that on the convention by which the noun is called the agent, the predicate is not called by the name of the object; rather, the noun is called both agent and noun, just as the predicate is called both object and predicate."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في الرضي: وحذفها لم يسمع إلا في مضارعاتها، وإنما جاز حذفها لعدم اللبس؛ إذ قد تقرر أنها لا تكون ناقصة إلا معها، ويحذف مع القسم كثيرا.",
     "en": "In al-Raḍī: “Its omission has been heard only with their imperfect forms; its omission is permitted only because there is no ambiguity, since it is established that they are incomplete only with it; and it is frequently omitted with an oath.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وللتعميم قال: ويلزمها النفي، ولم يقل: ويلزمها كلمة النفي.",
     "en": "For the sake of generality he said “and they necessarily take negation”, and did not say “and they necessarily take a negative particle”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة يوسف:٨٥.",
     "en": "Qurʾān, Sūrat Yūsuf 12:85."},
]
