# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 247 (printed ٢٤٦)."""

PAGE_NUMBER = 247
PRINTED_PAGE = "٢٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the definition of the mafʿūl maʿahu from PDF p. 246.
    {"type": "matn",
     "ar": "(هو مذكور بعد الواو) احتراز عن المذكور بعد غيره كالفاء[[١]]",
     "en": "(It is what is mentioned after the wāw), guarding against what is mentioned after another [particle], such as the fāʾ,"},
    {"type": "matn",
     "ar": "(لمصاحبة معمول فعل) اللام متعلق بـ«مذكور»[[٢]]، أي: يكون ذكره بعد الواو لأجل مصاحبته معمول فعل وإفادته إياها",
     "en": "(for accompanying what is governed by a verb): the lām is attached to “mentioned,” that is, its mention after the wāw is for the sake of its accompanying what is governed by a verb and of conveying that [accompaniment],"},
    {"type": "matn",
     "ar": "سواء كان ذلك المعمول[[٣]] فاعلا، نحو: «استوى الماء والخشبة»[[٤]]، أو مفعولا نحو: «كفاك وزيدا درهم»،",
     "en": "whether that governed element is an agent, as in “The water rose level with the post,” or an object, as in “A dirham suffices you along with Zayd”;"},
    {"type": "matn",
     "ar": "وسواء كان ذلك الفعل (لفظا) أي: لفظيا كالمثالين المذكورين (أو معنى) أي: معنويا، نحو: «ما لك وزيدا؟» أي: ما تصنع وزيدا،",
     "en": "and whether that verb is (in wording), that is, verbal, as in the two examples mentioned, (or in meaning), that is, notional, as in “What is with you and Zayd?”, that is, “What are you doing with Zayd?”"},
    {"type": "matn",
     "ar": "والمراد بمصاحبته لمعمول الفعل[[٥]] مشاركته له في ذلك الفعل في زمان واحد نحو: «سرت وزيدا»، أو مكان واحد[[٦]] نحو: «لو تركت الناقة[[٧]] وفصيلها لرضعتها»،",
     "en": "What is meant by its accompanying what is governed by the verb is its sharing with it in that action at one time, as in “I travelled along with Zayd,” or in one place, as in “Were the she-camel left with her young, it would suckle her.”"},
    {"type": "matn",
     "ar": "فلا ينتقض بالمذكور بعد الواو العاطفة نحو: «جاءني زيد وعمرو»، فإنها لا تدل إلا على المشاركة في أصل الفعل دون المصاحبة.",
     "en": "So [the definition] is not breached by what is mentioned after the conjunctive wāw, as in “Zayd and ʿAmr came to me,” for it indicates only sharing in the action itself, not accompaniment."},
    {"type": "matn",
     "ar": "اعلم أن مذهب جمهور النحاة[[٨]] أن العامل في المفعول معه الفعل أو معناه بتوسط الواو التي بمعنى «مع»،",
     "en": "Know that the doctrine of the majority of grammarians is that what governs the object of accompaniment is the verb, or its meaning, through the intermediary of the wāw meaning “with” (maʿa)."},
    {"type": "matn",
     "ar": "وإنما وضعوا «الواو» موضع «مع»؛ لكونها أخصر، وأصلها واو العطف[[٩]] التي فيها معنى الجمع، فناسب معنى المعية.",
     "en": "They put the wāw in place of “maʿa” only because it is shorter; its origin is the conjunctive wāw, which carries the meaning of combining, and so it suits the meaning of accompaniment."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يقتصر الاحتراز على ما ذكره، بل احتراز عما لم يذكر بعد شيء أيضا،",
     "en": "The guarding is not confined to what he mentioned; it also guards against what is not mentioned after anything."},
    {"type": "pair",
     "ar": "فالحق أن المقصود الاحتراز عن المذكور بعد «مع»، ولولاه لقال المذكور لمصاحبته إلى آخره.",
     "en": "The truth is that what is intended is to guard against what is mentioned after “maʿa”; were it not so, he would have said “what is mentioned for accompanying…” to the end."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه لطافة ولو قال: بالمذكور لكان ألطف، فتدبر.",
     "en": "There is subtlety in this; had he said “to the [word] mentioned,” it would have been subtler. So reflect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "شرط بعضهم كون المعمول فاعلا نظرا إلى أن «عمرا» في قوله: «ضربت زيدا وعمرا» معطوف اتفاقا لا مفعول معه.",
     "en": "Some stipulated that the governed element be an agent, in view of “ʿAmr” in the saying “I struck Zayd and ʿAmr” being, by agreement, conjoined, not an object of accompaniment."},
    {"type": "pair",
     "ar": "وينتقض ما قاله بنحو: «حسبك وزيدا»، فإن الكاف في المعنى مفعول؛ إذ المعنى: يكفيك.",
     "en": "What he said is breached by such a case as “Enough for you along with Zayd,” for the kāf is in meaning an object, since the meaning is “it suffices you.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: تساوى الماء والخشبة في العلو أي: وصل الماء إلى الخشبة، فليست الخشبة أرفع من الماء،",
     "en": "That is: the water and the post became equal in height, that is, the water reached the post, so the post is not higher than the water."},
    {"type": "pair",
     "ar": "والخشبة هنا مقياس يعرف به قدر ارتفاع الماء وقت زيادته.",
     "en": "The post here is a gauge by which the measure of the water’s rise is known at the time of its increase."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فلا يجوز ضحك زيد وطلوع الشمس كما ذهب إليه الأخفش،",
     "en": "So “Zayd laughed along with the sunrise” is not permissible, as al-Akhfash held;"},
    {"type": "pair",
     "ar": "ويجوز غيره استدلالا بقولهم: ما زلت أسير والنيل، فإن الماء لا يسير بل يجري.",
     "en": "others allow it, adducing their saying “I kept travelling along with the Nile,” for water does not travel but flows."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: المراد بالسير المعنى المجازي الشامل للسير والجريان.",
     "en": "It can be said that what is meant by travelling is the figurative sense covering both travelling and flowing."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المشهور الاكتفاء بوحدة الزمان.",
     "en": "The well-known view is that unity of time suffices."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "على صيغة المجهول.",
     "en": "In the passive form (turikat)."},
    {"type": "pair",
     "ar": "ولو جعلته صيغة معروفة لكان من باب «ضربت زيدا وعمرا»، ولم يكن مما نحن فيه.",
     "en": "Were you to make it active, it would belong to the type “I struck Zayd and ʿAmr,” and would not be of what we are concerned with."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قال عبد القاهر: هو منصوب بنفس الواو.",
     "en": "ʿAbd al-Qāhir said: it is put in the accusative by the wāw itself."},
    {"type": "pair",
     "ar": "وفيه أن الأولى رعاية أصل الواو في كونها غير عاملة، ولو نصبت بمعنى مع مطلقا لنصبت في كل رجل وضيعته.",
     "en": "Against this: it is better to respect the original nature of the wāw as non-governing; and if it governed the accusative in the sense of “with” without restriction, it would do so in “every man and his trade.”"},
    {"type": "pair",
     "ar": "وقال الأخفش: منصوب نصب الظروف؛ لأنها قامت مقام مع لكن لما كانت في الأصل حرفا أعطى النصب ما بعدها.",
     "en": "Al-Akhfash said: it is in the accusative as adverbs are, because [the wāw] stands in place of “maʿa”; but since it was originally a particle, the accusative was given to what follows it."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     # REVIEW: second «مصاحبة» printed with tāʾ marbūṭa; read as «مصاحبه» (its companion), like the first.
     "ar": "ولهذا لا يجوز تقديم المفعول معه على ما عمل في مصاحبه اتفاقا. ولا على مصاحبة خلافا لأبي الفتح.",
     "en": "For this reason it is not permissible, by agreement, to place the object of accompaniment before what governs its companion; nor before its companion, contrary to Abū al-Fatḥ."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا أرى منعا من تقديم المفعول معه على عامله إذا تأخر عن المصاحب كما",
     "en": "Shaykh al-Raḍī said: I see no bar to placing the object of accompaniment before its governor if it comes after the companion, as…"},
]
