# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 537 (printed ٥٣٦)."""

PAGE_NUMBER = 537
PRINTED_PAGE = "٥٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فـ«زيد» في هذا المثال: إما» at the foot of PDF p. 536 (mid-sentence).
    {"type": "matn",
     "ar": "مبتدأ و«نعم الرجل» مقدما عليه خبره، وإما خبر مبتدأ محذوف على تقدير سؤال،",
     "en": "…a subject, with “niʿma al-rajulu” as its predicate placed before it, or the predicate of an omitted subject, on the supposition of a question;"},
    {"type": "matn",
     "ar": "فإنه لما قيل: «نعم الرجل»، فكأنه سئل: «من هو؟» فقيل: «زيد» أي: هو زيد،",
     "en": "for when “niʿma al-rajulu” was said, it is as though it was asked “Who is he?”, and it was said “Zayd”, that is, “he is Zayd”."},
    {"type": "matn",
     "ar": "فعلى الوجه الأول: «نعم الرجل زيد» جملة واحدة، وعلى الوجه الثاني جملتان.",
     "en": "So on the first analysis “niʿma al-rajulu Zaydun” is one sentence, and on the second analysis two sentences."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط المخصوص، يعني: شرط صحة وقوعه مخصوصا (مطابقة الفاعل) أي: مطابقته الفاعل[[١]]،",
     "en": "(And its condition), that is, the condition of the specified term, meaning the condition for its validly occurring as the specified term, (is agreement with the agent), that is, its agreeing with the agent,"},
    {"type": "matn",
     "ar": "أو مطابقة الفاعل إياه في الجنس حقيقة أو تأويلا[[٢]] في الإفراد والتثنية والجمع والتذكير والتأنيث؛ لكونه عبارة عن الفاعل في المعنى",
     "en": "or the agent’s agreeing with it, in genus, really or by interpretation, in singular, dual and plural, and in masculine and feminine, because it denotes the agent in meaning;"},
    {"type": "matn",
     "ar": "نحو: «نعم الرجل زيد، ونعم الرجلان الزيدان، ونعم الرجال الزيدون، وبئست المرأة هند، وبئست المرأتان الهندان، وبئست النساء الهندات»،",
     "en": "as in “niʿma al-rajulu Zaydun”, “niʿma al-rajulāni al-Zaydāni”, “niʿma al-rijālu al-Zaydūna”, “biʾsati al-marʾatu Hindun”, “biʾsati al-marʾatāni al-Hindāni”, “biʾsati al-nisāʾu al-Hindātu”."},
    {"type": "matn",
     "ar": "ويجوز أن يقال: «نعم المرأة هند، وبئس المرأة هند»؛ لأنهما لما كانا غير متصرفين أشبها الحرف، فلم يجب إلحاق العلامة بهما.",
     "en": "It is permissible to say “niʿma al-marʾatu Hindun” and “biʾsa al-marʾatu Hindun”, because, since the two are not conjugated, they resemble the particle, so attaching the [feminine] marker to them is not obligatory."},
    {"type": "matn",
     "ar": "(و) قوله تعالى: (﴿بئس مثل القوم الذين كذبوا بآيات الله﴾[[٣]]) جواب سؤال",
     "en": "(And) His words, the Exalted: (“Evil is the likeness of the people who deny the signs of Allah”) is the answer to a question,"},
    {"type": "matn",
     "ar": "حيث وقع المخصوص -أعني «الذين كذبوا»- جمعا مع إفراد الفاعل -وهو «مثل القوم»-",
     "en": "since the specified term, namely “those who deny”, occurs as a plural while the agent, namely “mathalu al-qawmi”, is singular."},
    {"type": "matn",
     "ar": "(وشبهه) مما لا يطابق الفاعل المخصوص (متأول) بتقدير: «مثل الذين كذبوا» أو بجعل «الذين» صفة للقوم، وحذف المخصوص أي: «بئس مثل القوم المكذبين مثلهم».",
     "en": "(And what resembles it), where the agent does not agree with the specified term, (is interpreted), by supposing “the likeness of those who deny”, or by making “alladhīna” an adjective of “al-qawm” and omitting the specified term, that is, “evil is the likeness of the denying people: their likeness”."},
    {"type": "matn",
     "ar": "(وقد يحذف المخصوص إذا علم) بالقرينة (مثل) قوله تعالى: ﴿نعم العبد﴾ أي: «أيوب» بقرينة أن ذلك في قصته",
     "en": "(And the specified term is sometimes omitted when it is known) by a contextual indication, (as in) His words, the Exalted: “An excellent servant!”, that is, Ayyūb, indicated by this being in his story;"},
    {"type": "matn",
     "ar": "(و) قوله تعالى: ﴿فنعم الماهدون﴾ أي: نحن.",
     "en": "(and) His words, the Exalted: “and excellent are the spreaders!”, that is, We."},
    {"type": "matn",
     "ar": "(و«ساء» مثل «بئس») في إفادة الذم والشرائط والأحكام.",
     "en": "(And “sāʾa” is like “biʾsa”) in conveying blame, and in the conditions and rules."},
    {"type": "matn",
     "ar": "(ومنها) أي: من أفعال المدح والذم «حب» في («حبذا»، وهو) أي: «حبذا»",
     "en": "(And among them), that is, among the verbs of praise and blame, is “ḥabba” in (“ḥabbadhā”; and it), that is, “ḥabbadhā”, is"},
    {"type": "matn",
     "ar": "(مركب) من «حب الشيء» أو «حب»[[٤]] إذا صار محبوبا، ومن «ذا» (وفاعله) أي:",
     "en": "(compounded) of “ḥabba al-shayʾu” or “ḥabba”, [said] when a thing has become loved, and of “dhā”; (and its agent), that is,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: الفاعل يحتمل أن يكون فاعلا، ويحتمل أن يكون مفعولا.",
     "en": "He means: “al-fāʿil” [in “its agreeing with the agent”] may be the agent [of the verbal noun] and may be its object."},
    {"type": "pair",
     "ar": "وظني أن الملتبس بالفاعل يتعين للفاعل، كما إذا التبس فاعل الفعل بالمفعول يتعين المقدم للفاعل.",
     "en": "My view is that what is ambiguous with the agent is assigned to the agent, just as, when the agent of a verb is ambiguous with the object, the one placed first is assigned to the agent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يخص التعميم المطابقة في الجنس، بل يجري في المطابقة في غيره أيضا، فالأنسب تأخيره.",
     "en": "The generalization [“really or by interpretation”] is not peculiar to agreement in genus; it applies to agreement in other respects as well, so it would be more fitting to put it later."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الجمعة:٥.",
     "en": "Qurʾān, Sūrat al-Jumuʿa 62:5."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يريد أن في «حب» لغتين: «حب» بفتح الحاء كما هو القياس، وحب بضمها بنقل الضمة إلى الحاء، ثم الإدغام؛ إذ أصله «حبب» على وزن حسن.",
     "en": "He means that there are two dialectal forms of “ḥabba”: “ḥabba” with fatḥa on the ḥāʾ, as is the analogical rule, and “ḥubba” with ḍamma on it, by transferring the ḍamma to the ḥāʾ and then assimilating; for its original form is “ḥabuba”, on the pattern of ḥasuna."},
    {"type": "pair",
     "ar": "وفي الصحاح تفصيله.",
     "en": "Its detailed account is in al-Ṣiḥāḥ."},
    {"type": "pair",
     "ar": "وعند صاحب القاموس: «حب» اسم بمعنى الحبيب، و«ذا» فاعله أي: هو حبيب.",
     "en": "According to the author of al-Qāmūs, “ḥibb” is a noun meaning “beloved”, and “dhā” is its agent, that is, “he is beloved”."},
]
