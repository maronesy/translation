# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 460 (printed ٤٥٩)."""

PAGE_NUMBER = 460
PRINTED_PAGE = "٤٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… سواء وضع لتفضيل الفاعل أو لتفضيل المفعول، فإنه مشتق من» at the foot of PDF p. 459.
    {"type": "matn",
     "ar": "فعل الموصوف بزيادته على الغير في ذلك الفعل، واسم المفعول موضوع لمن وقع عليه الفعل فقط.",
     "en": "…the action of the one qualified, with his exceeding another in that action; whereas the passive participle is coined only for that upon which the action falls."},
    # REVIEW: the matn prints «الاخر» (bare alif, no madda); transcribed as printed.
    {"type": "matn",
     "ar": "(وصيغته من الثلاثي المجرد على) زنة («مفعول» كمضروب، ومن غيره) أي: من غير الثلاثي المجرد (على صيغة اسم الفاعل[[١]] بفتح ما قبل الاخر)",
     "en": "(Its form from the bare triliteral is on) the measure (“mafʿūl”, as in maḍrūb; and from other than it), that is, from other than the bare triliteral, (on the form of the active participle with a fatḥa on the penultimate letter),"},
    {"type": "matn",
     "ar": "لخفة الفتحة وكثرة المفعول (كـ«مستخرج») بفتح الراء.",
     "en": "because of the lightness of the fatḥa and the frequency of the passive participle, (as in “mustakhraj”) with a fatḥa on the rāʾ."},
    {"type": "matn",
     "ar": "(وأمره) أي: شأنه وحاله (في العمل) أي: عمل النصب (والاشتراط) أي: اشتراط عمله بأحد الزمانين، والاعتماد على صاحبه، أو الهمزة أو «ما»",
     "en": "(Its case), that is, its condition and state, (in governing), that is, governing the accusative, (and in the stipulation), that is, the stipulation of its governing on one of the two times, and on reliance on its possessor, or on the hamza or “mā”,"},
    {"type": "matn",
     "ar": "(كأمر اسم الفاعل) أي: مثل شأنه وحاله، وإذا كان معرفا باللام يعمل بمعنى الماضي أيضا،",
     "en": "(is like the case of the active participle), that is, like its condition and state; and when it is made definite with the lām it governs in the sense of the past as well."},
    {"type": "matn",
     "ar": "فهو يرفع ما يقوم مقام الفاعل، ولو كان هناك مفعول آخر يبقى على نصبه",
     "en": "It gives the nominative to what stands in place of the agent (nāʾib al-fāʿil), and if there is another object there, it remains in the accusative,"},
    {"type": "matn",
     "ar": "(نحو: «زيد معطى غلامه درهما») الآن أو غدا أو «المعطى غلامه درهما الآن أو غدا أو أمس».",
     "en": "(as in “Zayd, his slave is given a dirham”) now or tomorrow, or “the one whose slave is given a dirham now or tomorrow or yesterday”."},

    {"type": "section", "ar": "[الصفة المشبهة]",
     "en": "The Resembling Adjective"},

    {"type": "matn",
     "ar": "(الصفة المشبهة) باسم الفاعل من حيث إنها تثنى وتجمع وتذكر وتؤنث (ما اشتق من فعل لازم) احترازا عن اسم الفاعل واسم المفعول المتعديين",
     "en": "(The adjective resembling) the active participle (al-ṣifa al-mushabbaha), in that it takes the dual and plural and the masculine and feminine, (is what is derived from an intransitive verb), to exclude the transitive active participle and passive participle,"},
    {"type": "matn",
     "ar": "(لمن) أي: لما (قام به على معنى الثبوت) لا بمعنى الحدوث[[٢]]، احترازا عن نحو: «قائم وذاهب» مما اشتق من فعل لازم لمن قام به بمعنى الحدوث، فإنه اسم الفاعل لا صفة مشبهة،",
     "en": "(for that in which) [the action] (subsists, in the sense of permanence) (thubūt), not in the sense of occurrence (ḥudūth), to exclude such as “qāʾim” (standing) and “dhāhib” (going), which are derived from an intransitive verb for that in which [the action] subsists in the sense of occurrence; for that is an active participle, not a resembling adjective."},
    {"type": "matn",
     "ar": "واللازم أعم من أن يكون لازما ابتداء أو عند الاشتقاق كـ«رحيم»، فإنه مشتق من «رحم» بكسر العين بعد نقله[[٣]] إلى «رحم» بضمها،",
     "en": "“Intransitive” is more general than being intransitive from the outset or at the point of derivation, as with “raḥīm” (merciful); for it is derived from “raḥima”, with a kasra on the ʿayn, after its transfer to “raḥuma”, with a ḍamma on it;"},
    {"type": "matn",
     "ar": "فلا يقال: «رحيم» إلا من «رحم» بضم الحاء أي: صار الرحم طبيعة له، كـ«كرم» بمعنى: صار الكرم طبيعة له.",
     "en": "so “raḥīm” is said only from “raḥuma”, with a ḍamma on the ḥāʾ, that is, “mercy became a nature for him”, like “karuma”, meaning “generosity became a nature for him”."},
    {"type": "matn",
     "ar": "والمراد بكونه بمعنى الثبوت: أنه يكون كذلك بحسب أصل الوضع،",
     "en": "What is meant by its being in the sense of permanence is that it is so according to its original coinage;"},
    {"type": "matn",
     "ar": "فيخرج عنه نحو: «ضامر وطالق»؛ لأنهما بحسب أصل الوضع للحدوث، ثم عرض لهما الثبوت بحسب الاستعمال.",
     "en": "so such as “ḍāmir” (lean) and “ṭāliq” (divorced) are excluded from it, because by original coinage they are for occurrence, and permanence then accrued to them through usage."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وقد شذ نحو: أضعف فهو مضعوف، وأزكم فهو مزكوم، وأحم فهو محموم، وأحزن فهو محزون، وأحب فهو محبوب.",
     "en": "Anomalous are such as: “aḍʿafa”, so he is “maḍʿūf” (weakened); “azkama”, so he is “mazkūm” (afflicted with a cold); “aḥamma”, so he is “maḥmūm” (feverish); “aḥzana”, so he is “maḥzūn” (grieved); and “aḥabba”, so he is “maḥbūb” (beloved)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بالمعنى الذي مر في تعريف اسم الفاعل.",
     "en": "In the sense given in the definition of the active participle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولذا قالوا: أن فعيلا من فعل بفتح العين كقدير ونصير، ومن فعل بضم العين صفة مشبهة.",
     "en": "For this reason they said that faʿīl from faʿala, with a fatḥa on the ʿayn, as in “qadīr” and “naṣīr”, [is an active participle], and from faʿula, with a ḍamma on the ʿayn, [is] a resembling adjective."},
]
